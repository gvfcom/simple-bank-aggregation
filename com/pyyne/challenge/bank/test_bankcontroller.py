import os, sys; parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../..')); sys.path.append(parent_dir)

import datetime
from io import StringIO
from com.bank1.integration.Bank1AccountSource import Bank1AccountSource
from com.bank2.integration.Bank2AccountSource import Bank2AccountSource
from com.pyyne.challenge.bank.BankController import print_balances, print_transactions
from BankAdapter import Bank1Adapter, Bank2Adapter

import unittest
from io import StringIO
import sys

def test_print_balances():
    # Redirect the standard output to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the print_balances function
    print_balances()

    # Get the printed output
    printed_output = captured_output.getvalue().strip()

    # Define the expected output
    expected_output = """Bank 1 | Account ID: 12345 | Balance: 215.5 | Currency: USD
Bank 2 | Account ID: 12345 | Balance: 512.5 | Currency: USD"""

    # Assert that the printed output matches the expected output
    assert printed_output == expected_output, f"Expected:\n{expected_output}\nGot:\n{printed_output}"

    # Restore the standard output
    sys.stdout = sys.__stdout__


def test_print_transactions():
    # Redirect the standard output to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the print_transactions function
    print_transactions()

    # Get the printed output
    printed_output = captured_output.getvalue().strip()

    # Define the expected output
    expected_output = """Bank 1 | Account ID: 12345 | Amount: 100.0 | Type: CREDIT | Text: Check deposit
Bank 1 | Account ID: 12345 | Amount: 25.5 | Type: DEBIT | Text: Debit card purchase
Bank 1 | Account ID: 12345 | Amount: 225.0 | Type: DEBIT | Text: Rent payment
Bank 2 | Account ID: 12345 | Amount: 125.0 | Type: DEBIT | Text: Amazon.com
Bank 2 | Account ID: 12345 | Amount: 500.0 | Type: DEBIT | Text: Car insurance
Bank 2 | Account ID: 12345 | Amount: 800.0 | Type: CREDIT | Text: Salary"""

    # Assert that the printed output matches the expected output
    assert printed_output == expected_output, f"Expected:\n{expected_output}\nGot:\n{printed_output}"

    # Restore the standard output
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
    test_print_balances()
    test_print_transactions()