class Ddl(object):
    def __init__(self):
        pass

    def create_database(self, db_name):
        return """
        CREATE DATABASE {}
        """.format(
            db_name
        )

    def create_sui_dev_database(self, db_name):
        return """
        CREATE DATABASE IF NOT EXISTS sui_dev
        """.format(
            db_name
        )

    def create_raw_table(self, tb_name, db_name):
        return """
        CREATE TABLE IF NOT EXISTS {}.{} (
            raw_datas String
        ) ENGINE = MergeTree order by raw_datas;
        """.format(
            db_name, tb_name
        )
    
    def insert_data_to_table(self, db_name, tb_name, columns):
        return "INSERT INTO {}.{} {} VALUES ".format(db_name, tb_name, columns)
