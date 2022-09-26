from ast import arg
from asyncio import events
import logging
from operator import index
from core.websocket import websocket
from core.loadto.clickhouse import ClickhouseServices
from core.pubsub import gcp_pubsub
import argparse
from server.clickhouse import ClickhouseServer
from core.loadto.rocketset import RocketsetServices
from core.jrpc.jrpc import JrpcServices
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import time


def subscribe(web_socket_server_host, web_socket_server_port):
    clickhouse = ClickhouseServer()
    gcpPubsub = gcp_pubsub.GcpPubsub()
    clickhouse.init()
    ch_services = ClickhouseServices()
    ch_services.create_sui_dev_database()
    ch_services.create_sui_tale_raws()

    gcpPubsub.consume_payload(ch_services.insert_into_table, 3.0)


def subscribe_to_rocketset():
    rocketsetServices = RocketsetServices()
    gcpPubsub = gcp_pubsub.GcpPubsub()

    gcpPubsub.consume_payload(rocketsetServices.add_data, 3.0)


def batch_to_rocketset(
    url,
    batch_size=1000,
    filepath="output.log",
    inc=1000
):
    global lck

    def get_row_in_log():
        with open(filepath, "r") as f:
            last_index = int(f.read())
        return last_index

    def etl_process(start, end, fname):
        datas = jrpc_services.get_transactions_range(start, end)
        datas_result = jrpc_services.jrpc_post(datas["transactions_id"])

        logging.info(datas_result)

        if datas_result[id] != None:

            datas_result = [
                {"_id": data["result"]["certificate"]["transactionDigest"], "params": data}
                for data in datas_result
            ]
            rocketsetServices.add_data(datas_result)

            lck.acquire()
            with open(fname, "r") as f:
                last_index = f.read()

            last_index = int(last_index)

            if last_index < end:
                last_index = end

            with open(fname, "a") as f:
                f.seek(0)
                f.truncate()
                f.write(f"{last_index}")
            lck.release()

    jrpc_services = JrpcServices(url)
    rocketsetServices = RocketsetServices()

    # current_row = jrpc_services.get_total_transaction()
    current_row = batch_size
    processes = []

    # create the shared lock
    lck = Lock()

    # defile the shared file path
    last_index = get_row_in_log()

    index = 0

    if last_index > 0:
        index = last_index
    else:
        index = 1
    with ThreadPoolExecutor(max_workers=200) as executor:
        index = int(index)
        current_row = int(current_row)
        inc = int(inc)
        batch_size = int(batch_size)
        for start in range(index, current_row, inc):
            processes.append(
                executor.submit(
                    etl_process,
                    start,
                    start + inc,
                    filepath,
                )
            )

            # etl_process(start,start + inc,filepath)

    for task in as_completed(processes):
        print(task.result())

    current_row_in_node = jrpc_services.get_total_transaction()
    current_row_in_log = get_row_in_log()

    if current_row_in_node > current_row_in_log:
        current_row = current_row + batch_size
        batch_to_rocketset(url, current_row, filepath,inc)
    else:
        time.sleep(10)
        current_row_in_log = get_row_in_log()
        current_row = current_row + batch_size
        batch_to_rocketset(url,current_row, filepath,inc)


def publish(web_socket_server_host, web_socket_server_port):
    suiWs = websocket.SuiWs(
        "ws://{}:{}".format(web_socket_server_host, web_socket_server_port)
    )
    suiWs.process(
        '{"jsonrpc":"2.0", "id": 1, "method": "sui_subscribeTransaction", "params":["Any"]}'
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-ws", "--websocket-server", help="sui websocket server", default="34.70.238.35"
    )

    parser.add_argument(
        "-wp", "--websocket-port", help="sui websocket server port", default="9001"
    )

    parser.add_argument(
        "-bz", "--batch-size", help="batch size for insert data to dwh", default=5000
    )

    parser.add_argument("-e", "--event", help="publish or subscribe", default="publish")
    parser.add_argument(
        "-il",
        "--index-log",
        help="existing .log file for save data indexing log",
        default="output.log",
    )

    parser.add_argument(
        "-ic",
        "--incremental-get-from-node",
        help="batching from node maximum 3000",
        default=1000,
    )

    # Read arguments from command line
    args = parser.parse_args()

    web_socket_server_host = args.websocket_server
    web_socket_server_port = args.websocket_port
    event = args.event
    index_log = args.index_log
    batch_size = args.batch_size
    incremental_get_from_node = args.incremental_get_from_node

    if event == "publish":
        publish(web_socket_server_host, web_socket_server_port)
    elif event == "subscribe":
        batch_to_rocketset(
            "http://{}:{}".format(web_socket_server_host, web_socket_server_port),
            batch_size,
            index_log,
            incremental_get_from_node
        )
    else:
        print(
            "please choose a spesific event.\n please run python script.py --help for more information."
        )
