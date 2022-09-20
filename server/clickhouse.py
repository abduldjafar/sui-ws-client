from cmath import log
from http import client
from clickhouse_driver import connect,Client
from clickhouse_driver import errors
from clickhouse_driver.dbapi.errors import OperationalError as op_error
from queries.ddl import ddl
import os
from const import const
import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


class ClickhouseServer(object):
    def __init__(self):

        self.ch_host = os.environ["CH_HOST"]
        self.ch_user = os.environ["CH_USER"]
        self.ch_passwd = os.environ["CH_PASSWORD"]
        self.client = None
        self.conn = None
        self.cursor = None

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            logging.info("success execute query: %s" % query)
            return (None,const.SUCCESS_EXECUTE_QUERY_MESSAGE)
            
        except op_error as e:
            logging.error("error executing query: %s" % e)

            return (errors,const.FAILED_EXECUTE_QUERY_MESSAGE)

    def insert_data(self, query, data):
        try:
            self.cursor.execute(query, data)
            return (
                None,
                const.SUCCESS_EXECUTE_QUERY_MESSAGE,
            )
        except op_error as e:
            logging.error("error insert datas: %s" % e)

            return (
                op_error,
                const.OPERATIONAL_ERROR_MESSAGE,
            )

    def init(self):
        try:
            self.client = Client(self.ch_host)
            self.conn = connect(host=self.ch_host,user=self.ch_user,password=self.ch_passwd,database="default")
            self.cursor = self.conn.cursor()
        except errors.Error as e:
            print(e.message)
