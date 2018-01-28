import yaml

def load_yaml_file(file_path):
    with open(file_path, "r") as file:
        return yaml.load(file)

# TODO 適切な名前を考える.
def flatten(x):
    if x == None:
        return []
    return list(_flatten(x, leading_values=[]))

def _flatten(x, leading_values):
    if isinstance(x, (tuple, list, set)):
        for value in x:
            for values in _flatten(value, leading_values):
                yield values
    elif isinstance(x, dict):
        for key, value in x.items():
            for values in _flatten(value, leading_values + [key]):
                yield values
    else:
        yield leading_values + [x]

