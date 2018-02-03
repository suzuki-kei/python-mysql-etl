import os

from bigquery import generate_bigquery_table_schema_json
from connection_factory import ConnectionFactory
from table_defs import load_table_defs
from utilities.language import generate_paths
from utilities.language import load_yaml_file

def main():
    connection_factory = create_connection_factory()
    table_defs = create_table_defs(connection_factory)

    for table_def in table_defs:
        print(generate_bigquery_table_schema_json(table_def))

def config_file_path(name):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, "..", "..", ".."))
    return os.path.join(root_dir, "config", name)

def create_connection_factory():
    connection_params_list = load_yaml_file(config_file_path("databases.yml"))
    return ConnectionFactory(connection_params_list)

def create_table_defs(connection_factory):
    host_database_table_list = generate_paths(load_yaml_file(config_file_path("tables.yml")))
    return load_table_defs(host_database_table_list, connection_factory)

if __name__ == "__main__":
    main()

