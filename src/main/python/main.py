import os

from table_defs import load_table_defs

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    resources_dir = os.path.join(root_dir, "src", "main", "resources")
    table_defs_file_path = os.path.join(resources_dir, "tables.yml")

    for table_def in load_table_defs(table_defs_file_path):
        print(table_def)

if __name__ == "__main__":
    main()

