from collections import namedtuple

from closeable import Closeable

TableDef = namedtuple("TableDef", (
    "host",
    "database",
    "table",
    "column_defs",
))

ColumnDef = namedtuple("ColumnDef", (
    "table",
    "name",
    "data_type",
    "column_type",
    "default_value",
    "is_nullable",
    "is_primary_key",
))

def create_table_defs(host_database_table_list, connection_factory):
    return [create_table_def(host, database, table, connection_factory)
            for (host, database, table) in host_database_table_list]

def create_table_def(host, database, table, connection_factory):
    with Closeable(connection_factory.connect(host, database)) as connection:
        column_defs = create_column_defs(database, table, connection)
        return TableDef(host, database, table, column_defs)

def create_column_defs(database, table, connection):
    sql = """
        SELECT
            *
        FROM
            information_schema.COLUMNS
        WHERE
            TABLE_SCHEMA=%s
            AND TABLE_NAME=%s
        ORDER BY
            ORDINAL_POSITION
    """
    with Closeable(connection.cursor(dictionary=True)) as cursor:
        cursor.execute(sql, (database, table))
        return list(map(create_column_def, cursor.fetchall()))

def create_column_def(row):
    return ColumnDef(
        table          = row["TABLE_NAME"],
        name           = row["COLUMN_NAME"],
        data_type      = row["DATA_TYPE"],
        column_type    = row["COLUMN_TYPE"],
        default_value  = row["COLUMN_DEFAULT"],
        is_nullable    = row["IS_NULLABLE"] == "YES",
        is_primary_key = row["COLUMN_KEY"] == "PRI",
    )

