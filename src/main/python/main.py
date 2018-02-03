import os

from table_defs import load_table_defs

def main():
    table_defs = load_table_defs(config_file_path("tables.yml"))

    for table_def in table_defs:
        print(table_def)

def config_file_path(name):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, "..", "..", ".."))
    return os.path.join(root_dir, "config", name)

if __name__ == "__main__":
    main()

