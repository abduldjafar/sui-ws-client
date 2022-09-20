from asyncio import events
from core.websocket import websocket
from core.loadto.clickhouse import ClickhouseServices
from core.pubsub import gcp_pubsub
import argparse
from server.clickhouse import ClickhouseServer

def subscribe():
    clickhouse = ClickhouseServer()
    pubsub = gcp_pubsub.GcpPubsub()

    clickhouse.init()

    ch_services = ClickhouseServices(clickhouse)
    #ch_services.create_sui_dev_database()
    ch_services.create_sui_tale_raws()
    pubsub.consume_payload(ch_services.insert_into_table,10.0)


def publish(web_socket_server_host,web_socket_server_port):
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
        "-e", "--event", help="publish or subscribe", default="publish"
    )

    # Read arguments from command line
    args = parser.parse_args()

    web_socket_server_host = args.websocket_server
    web_socket_server_port = args.websocket_port
    event = args.event
    
    if event == 'publish':
        publish(web_socket_server_host,web_socket_server_port)
    elif event == 'subscribe':
        subscribe()
    else:
        print("please choose a spesific event.\n please run python script.py --help for more information.")
