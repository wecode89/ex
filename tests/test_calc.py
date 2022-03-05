import unittest
import sys, os
import unittest
from unittest.mock import patch
from io import StringIO
from src.calc import MortgageIO, MortgageCalculator


def read_file_into_string_io(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    print("filepath:  {}".format(filepath))

    print(filepath)

    f = open(filepath)
    string_io = StringIO(f.read())
    f.close()

    print("string io---> {}".format(string_io))
    return string_io


class TestMortgageCalculator(unittest.TestCase):
    @patch("sys.stdin", read_file_into_string_io('data/valid_input.txt'))
    def test_valid(self):
        # get args from stdin
        mortgage_io = MortgageIO()
        args = mortgage_io.get()

        # calculate monthly payment
        mortgage_calc = MortgageCalculator(**args)
        monthly_payment = mortgage_calc.get_monthly_payment()
        print("Monthly payment: ${:.2f}".format(monthly_payment))


