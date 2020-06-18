import unittest

from src.UniquesInList import Main


class TestMain(unittest.TestCase):
    def test_simple_list(self):
        print("Testing simple List")
        data = [0, 1, 2, 3]
        result = Main.count_unique(data)
        self.assertEqual(4, result)

    def test_complex_list(self):
        print("Testing Complex List")
        data = [0, 0, 1, 1, 1, 2, 2, 3, 3]
        result = Main.count_unique(data)
        self.assertEqual(4, result)

    def test_single_list(self):
        print("Testing Single List")
        data = [1]
        result = Main.count_unique(data)
        self.assertEqual(1, result)

    def test_emtpy_list(self):
        print("Testing Empty List")
        data = []
        result = Main.count_unique(data)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()