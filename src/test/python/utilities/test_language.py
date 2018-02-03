from unittest import main, TestCase

from utilities.language import generate_paths

class LanguageGeneratePathsTest(TestCase):

    def test_none_value(self):
        self.assertEqual([[None]], generate_paths(None))

    def test_scalar_value(self):
        self.assertEqual([[1]], generate_paths(1))

    def test_empty_tuple_value(self):
        self.assertEqual([], generate_paths(tuple()))

    def test_empty_list_value(self):
        self.assertEqual([], generate_paths(list()))

    def test_empty_set_value(self):
        self.assertEqual([], generate_paths(set()))

    def test_empty_dict_value(self):
        self.assertEqual([], generate_paths(dict()))

    def test_non_nested_tuple_value(self):
        self.assertEqual([[1]], generate_paths((1, )))
        self.assertEqual([[1], [2]], generate_paths((1, 2, )))
        self.assertEqual([[1], [2], [3]], generate_paths((1, 2, 3, )))

    def test_non_nested_list_value(self):
        self.assertEqual([[1]], generate_paths([1]))
        self.assertEqual([[1], [2]], generate_paths([1, 2]))
        self.assertEqual([[1], [2], [3]], generate_paths([1, 2, 3]))

    def test_non_nested_set_value(self):
        self.assertEqual([[1]], generate_paths(set([1])))
        self.assertEqual([[1], [2]], generate_paths(set([1, 2])))
        self.assertEqual([[1], [2], [3]], generate_paths(set([1, 2, 3])))

    def test_non_nested_dict_value(self):
        self.assertEqual(
            [["one", 1]],
            generate_paths({"one": 1}))
        self.assertEqual(
            [["one", 1], ["two", 2]],
            generate_paths({"one": 1, "two": 2}))
        self.assertEqual(
            [["one", 1], ["two", 2], ["three", 3]],
            generate_paths({"one": 1, "two": 2, "three": 3}))

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
            generate_paths({
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
            generate_paths({
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

