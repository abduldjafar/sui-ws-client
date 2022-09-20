import asyncio
import websockets
import ssl
import json
import pprint
from core.pubsub import gcp_pubsub


class SuiWs(object):
    def __init__(self, url):
        self.url = url
        self.pubsub = gcp_pubsub.GcpPubsub()

    async def get_datas(self, params):
        async with websockets.connect(self.url, ping_interval=None) as websocket:
            await websocket.send(params)
            while True:
                payload = await websocket.recv()
                print("===================================")
                payload = payload.replace("\\", "")
                self.pubsub.push_payload(payload)

    def process(
        self,
        params,
    ):
        asyncio.get_event_loop().run_until_complete(self.get_datas(params))
