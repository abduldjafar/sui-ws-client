from cmath import log
from email import message
from time import sleep
from queries.ddl import ddl
from server.clickhouse import ClickhouseServer
import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

class ClickhouseServices(object):
    def __init__(self):
        self.query = ddl.Ddl()
        #self.clickhouse = ch_server
        self.db_name = "sui_dev"
        self.tb_name = "raw_transactions"
        self.columns = "(raw_datas)"
        self.ch_server = ClickhouseServer()
        self.ch_server.init()

    def create_sui_dev_database(self):
        
        create_database_query = self.query.create_database(self.db_name)
        err,message = self.ch_server.execute_query(create_database_query)

        return (err,message)
    
    def create_sui_tale_raws(self):

        create_table_query = self.query.create_raw_table(self.tb_name,self.db_name)
        err_create_table,message_reate_table= self.ch_server.execute_query(create_table_query)
        logging.info(message_reate_table)


    def insert_into_table(self, message):
        ch_server = ClickhouseServer()
        ch_server.init()
        datas = [{ "raw_datas" : str(message.data).replace("\\","") }]
        insert_datas_query = self.query.insert_data_to_table(self.db_name,self.tb_name,self.columns)

       
        err_insert_datas, message_insert_datas =  ch_server.insert_data(insert_datas_query,datas)
        logging.info(message_insert_datas)

        

        
         