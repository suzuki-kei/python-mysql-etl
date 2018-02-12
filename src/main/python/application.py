import os
from argparse import ArgumentParser

import bigquery
import table_defs
from connection_factory import ConnectionFactory
from utilities import generate_paths
from utilities import load_yaml_file

class Application(object):

    def __init__(self):
        arguments = self._parse_command_line_arguments()
        self._config = self._load_config(arguments.config_dir)

    def _parse_command_line_arguments(self):
        parser = ArgumentParser()
        parser.add_argument("-c", "--config-dir")
        return parser.parse_args()

    def _load_config(self, config_dir):
        config = load_yaml_file(os.path.join(config_dir, "application.yml"))
        config["work_dir"] = os.path.abspath(config["work_dir"])
        config["databases"] = load_yaml_file(os.path.join(config_dir, "databases.yml"))
        config["tables"] = load_yaml_file(os.path.join(config_dir, "tables.yml"))
        return config

    def run(self):
        connection_factory = self._create_connection_factory()
        table_defs = self._create_table_defs(connection_factory)
        for table_def in table_defs:
            #print(bigquery.generate_table_schema_json(table_def))
            output_file_name = "{}.{}.json".format(table_def.database, table_def.table)
            output_file_path = os.path.join(self._config["work_dir"], output_file_name)
            print(output_file_path)

    def _create_connection_factory(self):
        return ConnectionFactory(self._config["databases"])

    def _create_table_defs(self, connection_factory):
        host_db_table_list = generate_paths(self._config["tables"])
        return table_defs.create_table_defs(host_db_table_list, connection_factory)

def main():
    Application().run()

if __name__ == "__main__":
    main()

