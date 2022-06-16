import unittest
from task import *


class TestTask(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(10, skaiciu_suma(3, 3, 4))
        self.assertEqual(-10, skaiciu_suma(-2, -2, -6))
        self.assertEqual(2, skaiciu_suma(-3, -5, 10))

    def test_saraso_suma(self):
        list1 = [6, 0, 1, 5]
        list2 = [7, 4, 3, 2]
        list3 = [1]
        self.assertEqual(12, saraso_suma(list1))
        self.assertEqual(16, saraso_suma(list2))
        self.assertEqual(1, saraso_suma(list3))


if __name__ == '__main__':
    unittest.main()