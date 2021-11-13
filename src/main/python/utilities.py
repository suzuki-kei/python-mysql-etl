import yaml

def load_yaml_file(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def generate_paths(x):
    """dict 値を木構造とみなし, 各リーフノード (非コレクション値) までのパスを列挙する.

        入力例:
            {
                "hoge": {
                    "taro": [1, 2, 3]
                },
                "piyo": [
                    4,
                    {"fuga": 5},
                    {"gofu":
                        {"hanako": [6, 7, 8]}
                    }
                ]
            }

        出力例:
            [
                ["hoge", "taro", 1],
                ["hoge", "taro", 2],
                ["hoge", "taro", 3],
                ["piyo", 4],
                ["piyo", "fuga", 5],
                ["piyo", "gofu", "hanako", 6],
                ["piyo", "gofu", "hanako", 7],
                ["piyo", "gofu", "hanako", 8],
            ]
    """
    return list(_generate_paths(x, leading_values=[]))

def _generate_paths(x, leading_values=[]):
    if isinstance(x, (tuple, list, set)):
        for value in x:
            for values in _generate_paths(value, leading_values):
                yield values
    elif isinstance(x, dict):
        for key, value in x.items():
            for values in _generate_paths(value, leading_values + [key]):
                yield values
    else:
        yield leading_values + [x]

