import unittest
from keliamieji import *

class TestKeliamieji(unittest.TestCase):

    def test_ar_keliamieji(self):
        rezultatas = ar_keliamieji(2000)
        lukestis = False
        self.assertEqual(lukestis, rezultatas)

    def test_ar_keliamieji3(self):
        rezultatas = ar_keliamieji(1976)
        lukestis = False
        self.assertEqual(lukestis, rezultatas)

if __name__ == '__main__':
    unittest.main()