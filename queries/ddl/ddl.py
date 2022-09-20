class Ddl(object):
    def __init__(self):
        pass

    def create_database(self, db_name):
        return """
        CREATE DATABASE {}
        """.format(
            db_name
        )

    def create_stats_database(self, db_name):
        return """
        CREATE DATABASE {}_stats
        """.format(
            db_name
        )

    def create_table_sources(self, tb_name, db_name):
        return """
        CREATE TABLE IF NOT EXISTS {}.{} (
            source_id String,
            source	Nullable(String),
            medium	Nullable(String),
            campaign	Nullable(String),
            term	Nullable(String),
            referrer	Nullable(String),
            referrer_path Nullable(String),
        ) ENGINE = MergeTree order by source_id;
        """.format(
            db_name, tb_name
        )
