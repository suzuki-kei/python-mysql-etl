import os
from collections import namedtuple

import yaml
import mysql.connector

from utilities.closeable import Closeable
from utilities.language import generate_paths
from utilities.language import load_yaml_file

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    resources_dir = os.path.join(root_dir, "src", "main", "resources")
    table_defs_file_path = os.path.join(resources_dir, "table-defs.yml")

    for table_def in load_table_defs(table_defs_file_path):
        print(table_def)

TableDef = namedtuple("TableDef", (
    "host",
    "database",
    "table",
    "columns",
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

def load_table_defs(table_defs_file_path):
    def create_table_def(host, database, table):
        connection = create_connection(host)
        with Closeable(connection):
            column_defs = get_column_defs(connection, database, table)
            print(column_defs)
            return TableDef(host, database, table, column_defs)
    return [create_table_def(host, database, table)
            for (host, database, table)
            in generate_paths(load_yaml_file(table_defs_file_path))]

# TODO host 以外が決め打ちになっている.
def create_connection(host):
    return mysql.connector.connect(
        host=host,
        user="hoge",
        password="hoge",
        database="hoge",
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci",
    )

def get_column_defs(connection, database, table):
    def column_def_from_row(row):
        return ColumnDef(
            table          = row["TABLE_NAME"],
            name           = row["COLUMN_NAME"],
            data_type      = row["DATA_TYPE"],
            column_type    = row["COLUMN_TYPE"],
            default_value  = row["COLUMN_DEFAULT"],
            is_nullable    = row["IS_NULLABLE"] == "YES",
            is_primary_key = row["COLUMN_KEY"] == "PRI",
        )
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
    cursor = connection.cursor(dictionary=True)
    with Closeable(cursor):
        cursor.execute(sql, (database, table))
        return list(map(column_def_from_row, cursor.fetchall()))

if __name__ == "__main__":
    main()

