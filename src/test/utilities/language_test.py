from unittest import main, TestCase

from utilities.language import flatten

class LanguageFlattenTest(TestCase):

    def test_none_value(self):
        self.assertEqual([], flatten(None))

    def test_empty_tuple_value(self):
        self.assertEqual([], flatten(tuple()))

    def test_empty_list_value(self):
        self.assertEqual([], flatten(list()))

    def test_empty_set_value(self):
        self.assertEqual([], flatten(set()))

    def test_empty_dict_value(self):
        self.assertEqual([], flatten(dict()))

    def test_non_nested_tuple_value(self):
        self.assertEqual([[1]], flatten((1, )))
        self.assertEqual([[1], [2]], flatten((1, 2, )))
        self.assertEqual([[1], [2], [3]], flatten((1, 2, 3, )))

    def test_non_nested_list_value(self):
        self.assertEqual([[1]], flatten([1]))
        self.assertEqual([[1], [2]], flatten([1, 2]))
        self.assertEqual([[1], [2], [3]], flatten([1, 2, 3]))

    def test_non_nested_set_value(self):
        self.assertEqual([[1]], flatten(set([1])))
        self.assertEqual([[1], [2]], flatten(set([1, 2])))
        self.assertEqual([[1], [2], [3]], flatten(set([1, 2, 3])))

    def test_non_nested_dict_value(self):
        self.assertEqual(
            [["one", 1]],
            flatten({"one": 1}))
        self.assertEqual(
            [["one", 1], ["two", 2]],
            flatten({"one": 1, "two": 2}))
        self.assertEqual(
            [["one", 1], ["two", 2], ["three", 3]],
            flatten({"one": 1, "two": 2, "three": 3}))

    def test_nested_tuple_value(self):
        pass

    def test_nested_list_value(self):
        pass

    def test_nested_set_value(self):
        pass

    def test_nested_dict_value(self):
        self.assertEqual(
            [
                ["hoge", "taro", 1],
                ["hoge", "jiro", 2],
                ["piyo", "hanako", 3],
            ],
            flatten({
                "hoge": {
                    "taro": 1,
                    "jiro": 2,
                },
                "piyo": {
                    "hanako": 3,
                }
            }))
        self.assertEqual(
            [
                ["hoge", "taro", 1],
                ["hoge", "taro", 2],
                ["hoge", "taro", 3],
                ["piyo", 4],
                ["piyo", "fuga", 5],
                ["piyo", "gofu", "hanako", 6],
                ["piyo", "gofu", "hanako", 7],
                ["piyo", "gofu", "hanako", 8],
            ],
            flatten({
                "hoge": {
                    "taro": [1, 2, 3],
                },
                "piyo": [
                    4,
                    {"fuga": 5},
                    {"gofu": {"hanako": [6, 7, 8]}},
                ],
            }))
    
if __name__ == "__main__":
    main()

