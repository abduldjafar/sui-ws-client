import json
import os
import time
from rockset import RocksetClient, exceptions,models,QueryPaginator
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
            message_key = dict_log["message_key"]

            if message_key == "WRITE_RATE_LIMIT":
                logging.info("waiting 60s for documents to be added...")
                time.sleep(60)
                self.add_data(messages)

            elif message_key == "LONG_VALUE_OUT_OF_RANGE":
                logging.error(message_key)
            else:
                for message in messages:
                    try:
                        self.client.Documents.add_documents(
                            collection=self.collection_name,
                            data=[message],
                            workspace=self.workspace,
                        )
                    except exceptions.BadRequestException as e:
                        logging.error(e.body)

    def get_datas(self, start, end):
        pass

    def get_object_id_datas(self):
        try:
            rs = self.client.Queries.query(
                sql={
                    "query": """
            INSERT INTO sui.objectId_temp
            select 
                objectId as _id 
            from sui.transactions_result_event t
            where objectId is not null
            """,
                },
            )
            logging.info(rs)
            self.get_object_id_datas()
        except exceptions.ApiException as e:
            logging.error("Exception when querying: %s\n" % e)

    def pull_object_id_datas(self):
        for page in QueryPaginator(
            self.client,
            self.client.Queries.query(
                sql=models.QueryRequestSql(
                    query="""
                    select 
                        _id 
                    from sui.objectId_temp
                    """,
                    paginate=True,
                    initial_paginate_response_doc_count=3000,
                )
            ),
        ):
            yield page