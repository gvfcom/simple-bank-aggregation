from typing import List, Optional
import datetime

import os, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../..')); sys.path.append(parent_dir)
from BankTransactionAdapter import BankTransactionAdapter
from com.bank1.integration.Bank1AccountSource import Bank1AccountSource
from com.bank2.integration.Bank2AccountSource import Bank2AccountSource as Bank2Source
from com.bank1.integration.Bank1Transaction import Bank1Transaction
from com.bank2.integration.Bank2AccountTransaction import Bank2AccountTransaction
from BankTransactionAdapter import Bank1TransactionAdapter, Bank2TransactionAdapter

class BankAdapter:
    def getAccountBalance(self, accountId: int) -> Optional[float]:
        """
        Get the account balance for the given account ID.

        Args:
            accountId (int): The account ID.

        Returns:
            Optional[float]: The account balance.
        """
        raise NotImplementedError()
    
    def getCurrency(self, accountId: int) -> Optional[str]:
        """
        Get the account currency for the given account ID.

        Args:
            accountId (int): The account ID.

        Returns:
            Optional[str]: The account currency.
        """
        raise NotImplementedError()

    def getTransactions(self, accountId: int, from_date: datetime.date, to_date: datetime.date) -> List[BankTransactionAdapter]:
        """
        Get the list of transactions for the given account ID and date range.

        Args:
            accountId (int): The account ID.
            from_date (datetime.date): The start date of the date range.
            to_date (datetime.date): The end date of the date range.

        Returns:
            List[BankTransactionAdapter]: The list of transactions.
        """
        raise NotImplementedError()

class Bank1Adapter(BankAdapter):
    def __init__(self, bank1_source: Bank1AccountSource):
        self.bank1_source = bank1_source
        
    def getAccountBalance(self, accountId: int) -> Optional[float]:
        """
        Get the account balance for the given account ID.

        Args:
            accountId (int): The account ID.

        Returns:
            Optional[float]: The account balance.
        """
        return self.bank1_source.getAccountBalance(accountId)
    
    def getCurrency(self, accountId: int) -> Optional[str]:
        """
        Get the account currency for the given account ID.

        Args:
            accountId (int): The account ID.

        Returns:
            Optional[str]: The account currency.
        """
        return self.bank1_source.getAccountCurrency(accountId)

    def getTransactions(self, accountId: int, from_date: datetime.date, to_date: datetime.date)  -> List[Bank1TransactionAdapter]:
        """
        Get the list of transactions for the given account ID and date range.

        Args:
            accountId (int): The account ID.
            from_date (datetime.date): The start date of the date range.
            to_date (datetime.date): The end date of the date range.

        Returns:
            List[Bank1TransactionAdapter]: The list of transactions.
        """
        bank1_transaction_adapters = []
        for bank1_transaction in self.bank1_source.getTransactions(accountId, from_date, to_date):
            bank1_transaction_adapters.append(Bank1TransactionAdapter(bank1_transaction))

        return bank1_transaction_adapters

class Bank2Adapter(BankAdapter):
    def __init__(self, bank2_source: Bank2Source):
        self.bank2_source = bank2_source

    def getAccountBalance(self, accountId: int) -> Optional[float]:
        """
        Get the account balance for the given account ID.

        Args:
            accountId (int): The account ID.

        Returns:
            Optional[float]: The account balance.
        """
        balance = self.bank2_source.getBalance(accountNum=accountId)
        return balance.getBalance() if balance else None

    def getCurrency(self, accountId: int) -> Optional[str]:
        """
        Get the account currency for the given account ID.

        Args:
            accountId (int): The account ID.

        Returns:
            Optional[str]: The account currency.
        """
        return self.bank2_source.getBalance(accountId).getCurrency()

    def getTransactions(self, accountId: int, from_date: datetime.date, to_date: datetime.date) -> List[Bank2TransactionAdapter]:
        """
        Get the list of transactions for the given account ID and date range.

        Args:
            accountId (int): The account ID.
            from_date (datetime.date): The start date of the date range.
            to_date (datetime.date): The end date of the date range.

        Returns:
            List[Bank2TransactionAdapter]: The list of transactions.
        """
        bank2_transaction_adapters = []
        for bank2_transaction in self.bank2_source.getTransactions(accountId, from_date, to_date):
            bank2_transaction_adapters.append(Bank2TransactionAdapter(bank2_transaction))

        return bank2_transaction_adapters