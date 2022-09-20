from core.websocket import websocket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-ws", "--websocket-server", help="sui websocket server", default="34.70.238.35"
    )

    parser.add_argument(
        "-wp", "--websocket-port", help="sui websocket server port", default="9001"
    )

    # Read arguments from command line
    args = parser.parse_args()

    web_socket_server_host = args.websocket_server
    web_socket_server_port = args.websocket_port

    suiWs = websocket.SuiWs(
        "ws://{}:{}".format(web_socket_server_host, web_socket_server_port)
    )
    suiWs.process(
        '{"jsonrpc":"2.0", "id": 1, "method": "sui_subscribeTransaction", "params":["Any"]}'
    )
