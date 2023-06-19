# com/pyyne/challenge/bank/BankController.java
# Controller that pulls information form multiple bank integrations and prints them to the console.
# Created by Par Renyard on 5/12/21.

import os, sys; parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../..')); sys.path.append(parent_dir)
import datetime
from com.bank1.integration.Bank1AccountSource import Bank1AccountSource
from com.bank2.integration.Bank2AccountSource import Bank2AccountSource
from BankAdapter import Bank1Adapter, Bank2Adapter

def print_balances() -> None:
    """
    Print the account balances from all available bank integrations.
    """
    bank1_account_source = Bank1AccountSource()
    bank2_account_source = Bank2AccountSource()

    # Adapt Bank1AccountSource and Bank2AccountSource to the common AccountSource interface
    adapter1 = Bank1Adapter(bank1_account_source)
    adapter2 = Bank2Adapter(bank2_account_source)

    # Get the balances from all available bank integrations
    balance1 = adapter1.getAccountBalance(accountId=12345)
    currency1 = adapter1.getCurrency(accountId=12345)
    balance2 = adapter2.getAccountBalance(accountId=12345)
    currency2 = adapter2.getCurrency(accountId=12345)

    # Print the balances
    print(f"Bank 1 | Account ID: 12345 | Balance: {balance1} | Currency: {currency1}")
    print(f"Bank 2 | Account ID: 12345 | Balance: {balance2} | Currency: {currency2}")

def print_transactions() -> None:
    """
    Print the transactions from all available bank integrations.
    """
    bank1_account_source = Bank1AccountSource()
    bank2_account_source = Bank2AccountSource()

    # Adapt Bank1AccountSource and Bank2AccountSource to the common AccountSource interface
    adapter1 = Bank1Adapter(bank1_account_source)
    adapter2 = Bank2Adapter(bank2_account_source)

    # Get the transactions from all available bank integrations
    bank1_transactions = adapter1.getTransactions(
        accountId=12345, from_date=datetime.date(2023, 6, 1), to_date=datetime.date(2023, 6, 30)
    )
    
    for transaction in bank1_transactions:
        print(f"Bank 1 | Account ID: 12345 | Amount: {transaction.getAmount()} | Type: {transaction.getType()} | Text: {transaction.getText()}")

    bank2_transactions = adapter2.getTransactions(
        accountId=12345, from_date=datetime.date(2023, 6, 1), to_date=datetime.date(2023, 6, 30)
    )

    for transaction in bank2_transactions:
        print(f"Bank 2 | Account ID: 12345 | Amount: {transaction.getAmount()} | Type: {transaction.getType()} | Text: {transaction.getText()}")

# Print balances and transactions
if __name__ == '__main__':
    print_balances()
    print_transactions()

    import unittest