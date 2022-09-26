import asyncio
import websockets
from core.pubsub import gcp_pubsub
from concurrent.futures import ThreadPoolExecutor, as_completed
from core.loadto.clickhouse import ClickhouseServices


class SuiWs(object):
    def __init__(self, url):
        self.url = url
        self.pubsub = gcp_pubsub.GcpPubsub()

    async def get_datas(self, params):
        process = []
        with ThreadPoolExecutor(max_workers=200) as executor:
            async with websockets.connect(self.url, ping_interval=None) as websocket:
                await websocket.send(params)
                while True:
                    payload = await websocket.recv()
                    print("===================================")
                    payload = payload.replace("\\", "")
                    # self.pubsub.push_payload(payload)
                    process.append(executor.submit(self.pubsub.push_payload, payload))

    async def ingestion_to_clickhouse(self, params):
        process = []

        def insert_to_clickhouse(datas):
            ch_services = ClickhouseServices()
            ch_services.insert_into_table(datas)

        with ThreadPoolExecutor(max_workers=200) as executor:
            async with websockets.connect(self.url, ping_interval=None) as websocket:
                await websocket.send(params)
                while True:
                    payload = await websocket.recv()
                    print("===================================")
                    payload = payload.replace("\\", "")
                    # self.pubsub.push_payload(payload)
                    process.append(executor.submit(insert_to_clickhouse, payload))

    def process(
        self,
        params,
    ):
        asyncio.get_event_loop().run_until_complete(self.get_datas(params))

    def process_ingestion_to_clickhouse(
        self,
        datas,
    ):
        asyncio.get_event_loop().run_until_complete(self.ingestion_to_clickhouse(datas))
