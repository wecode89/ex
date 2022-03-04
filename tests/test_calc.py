import unittest
import sys, os
from src.calc import MortgageIO, MortgageCalculator


class TestBase(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.path = self.path.replace('/tests', '')
        sys.path.append(self.path)

    def tearDown(self):
        del self.calc

    def test_valid(self):
        pass

    def test_invalid(self):
        pass

    def test_null(self):
        pass


class TestMortgageCalculator(unittest.TestCase):

    def test_valid(self):

        number = MortgageCalculator(1000, 0.05, 30, 0.0).get_monthly_payment()
        self.assertEqual(number, 105.0)

