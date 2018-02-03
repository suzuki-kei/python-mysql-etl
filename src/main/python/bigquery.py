import json

def generate_table_schema_json(table_def):
    columns = list(map(to_bigquery_column_def, table_def.column_defs))
    return json.dumps(columns, indent=4)

def to_bigquery_column_def(column_def):
    return {
        "name": column_def.name,
        "type": to_bigquery_column_type(column_def.data_type),
        "required": column_def.is_nullable == False,
    }

def to_bigquery_column_type(mysql_column_type):
    return {
        "int":        "integer",
        "tinyint":    "integer",
        "smallint":   "integer",
        "mediumint":  "integer",
        "bigint":     "integer",
        "float":      "float",
        "double":     "float",
        "decimal":    "float",
        "varchar":    "string",
        "char":       "string",
        "text":       "string",
        "tinytext":   "string",
        "mediumtext": "string",
        "longtext":   "string",
        "time":       "time",
        "date":       "date",
        "timestamp":  "timestamp",
        "datetime":   "timestamp",
        "date":       "timestamp",
        "set":        "string",
        "enum":       "string",
    }.get(mysql_column_type, "string")

