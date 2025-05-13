# write function tests here, don't add input('') statements here!
import unittest

from src.question_a.question_a import test_config as test_config_a
from src.question_b.question_b import test_config as test_config_b, get_most_likely_ancestor_consensus
from src.question_c.question_c import test_config as test_config_c, get_stock_list
from src.question_d.question_d import test_config as test_config_d, create_multiplication_table

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config_a())

    def test_question_b_config(self):
        self.assertEqual(True, test_config_b())

    def test_question_c_config(self):
        self.assertEqual(True, test_config_c())

    def test_question_d_config(self):
        self.assertEqual(True, test_config_d())


class Test_Question_B(unittest.TestCase):

    def test_substring_locations(self):
        result = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        self.assertEqual(result, (2, 4, 10))


class Test_Question_C(unittest.TestCase):

    def test_stock_list_length(self):
        stock_list = get_stock_list()
        self.assertEqual(len(stock_list), 5)

    def test_stock_list_contents(self):
        stock_list = get_stock_list()
        symbols = [stock.get_symbol() for stock in stock_list]
        self.assertIn("AAPL", symbols)
        self.assertIn("MSFT", symbols)
        self.assertIn("GOOG", symbols)


class Test_Question_D(unittest.TestCase):

    def test_multiplication_table_size(self):
        table = create_multiplication_table()
        self.assertEqual(len(table), 5)
        for row in table:
            self.assertEqual(len(row), 10)

    def test_multiplication_table_values(self):
        table = create_multiplication_table()
        self.assertEqual(table[0][0], 1)     # 1x1
        self.assertEqual(table[1][1], 4)     # 2x2
        self.assertEqual(table[4][9], 50)    # 5x10


if __name__ == '__main__':
    unittest.main()
