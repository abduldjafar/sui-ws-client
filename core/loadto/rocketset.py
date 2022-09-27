import json
import os
import time
from rockset import RocksetClient, exceptions
import logging


class RocketsetServices(object):
    def __init__(self):
        # connect securely to Rockset production API servers
        self.host = (
            "localhost"
            if os.environ.get("ROCKETSET_HOST") == None
            else os.environ["ROCKETSET_HOST"]
        )
        self.api_key = (
            "ROCKETSET_API_KEY"
            if os.environ.get("ROCKETSET_API_KEY") == None
            else os.environ["ROCKETSET_API_KEY"]
        )
        self.client = RocksetClient(host=self.host, api_key=self.api_key)
        self.collection_name = (
            "ROCKETSET_COLLECTION_NAME"
            if os.environ.get("ROCKETSET_COLLECTION_NAME") == None
            else os.environ["ROCKETSET_COLLECTION_NAME"]
        )
        self.workspace = (
            "ROCKETSET_WORKSPACE_NAME"
            if os.environ.get("ROCKETSET_WORKSPACE_NAME") == None
            else os.environ["ROCKETSET_WORKSPACE_NAME"]
        )

    def add_data(self, messages):
        if type(messages) != list:
            messages = [messages]
        try:
            push = self.client.Documents.add_documents(
                collection=self.collection_name, data=messages, workspace=self.workspace
            )
            logging.info("Added documents to collection success")

        except exceptions.BadRequestException as e:
            logging.error(e.body)
            dict_log = json.loads(e.body)
            
            if dict_log["message_key"] == "WRITE_RATE_LIMIT":
                logging.info("waiting 60s for documents to be added...")
                time.sleep(60)
                self.add_data(messages)
            else:
                for message in messages:
                    logging.info(message)
                    self.client.Documents.add_documents(
                        collection=self.collection_name,
                        data=[message],
                        workspace=self.workspace,
                    )
