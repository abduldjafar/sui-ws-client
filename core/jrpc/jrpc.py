import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from rockset import RocksetClient
import logging


class JrpcServices(object):
    def __init__(self, url):
        self.url = url

        self.get_total_transaction_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "sui_getTotalTransactionNumber",
            "params": [],
        }

        self.transaction_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "sui_getTransaction",
            "params": [""],
        }

        self.transaction_by_range_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "sui_getTransactionsInRange",
            "params": [0, 0],
        }

    def jrpc_post(self, payload):
        headers = {"Content-Type": "application/json"}
        response = requests.request(
            "POST", self.url, data=json.dumps(payload), headers=headers
        )
        data = json.loads(response.text)
        return data

    def get_total_transaction(self):
        post = self.jrpc_post(self.get_total_transaction_payload)
        return post["result"]

    def get_transactions_range(self, first, last):
        def setup_transaction_payload(transaction_id):
            return {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "sui_getTransaction",
                "params": [transaction_id],
            }

        result = {"last_index": 0, "transactions_id": []}
        self.transaction_by_range_payload["params"][0] = first
        self.transaction_by_range_payload["params"][1] = last
        post = self.jrpc_post(self.transaction_by_range_payload)

        result["last_index"] = post["result"][-1][0]
        result["transactions_id"] = [
            setup_transaction_payload(data[1]) for data in post["result"]
        ]

        return result

    def get_transactions_datas(self, transactions_id):
        datas = []
        for transaction_id in transactions_id:
            self.transaction_payload["params"][0] = transaction_id
            data = self.jrpc_post(self.transaction_payload)
            datas.append(data)

        return data

    def get_transactions_data(self, transaction_id):
        self.transaction_payload["params"][0] = transaction_id
        return self.jrpc_post(self.transaction_payload)

    def extract_id(self, firts, last):
        inc = 1
        if last >= 100:
            inc = 100
        for first in range(firts, last + 1, inc):
            yield self.get_transactions_range(first, first + inc)

    def extract_datas(self, firts, last):
        for data in self.extract_id(firts, last):
            yield self.get_transactions_datas(data["transactions_id"])