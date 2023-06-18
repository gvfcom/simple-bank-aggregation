# com/bank1/integration/Bank1AccountSource.java
# Created by Par Renyard on 5/12/21.

from typing import List, Optional
import datetime

from com.bank1.integration.Bank1Transaction import Bank1Transaction

class Bank1AccountSource:
    def getAccountBalance(self, accountId: int) -> Optional[float]:
        """
        Get the account balance for the given account ID.

        Args:
            accountId (int): The account ID.

        Returns:
            Optional[float]: The account balance.
        """
        return 215.5

    def getAccountCurrency(self, accountId: int) -> Optional[str]:
        """
        Get the account currency for the given account ID.

        Args:
            accountId (int): The account ID.

        Returns:
            Optional[str]: The account currency.
        """
        return "USD"

    def getTransactions(
        self, accountId: int, fromDate: datetime.date, toDate: datetime.date
    ) -> List[Bank1Transaction]:
        """
        Get the list of transactions for the given account ID and date range.

        Args:
            accountId (int): The account ID.
            fromDate (datetime.date): The start date of the date range.
            toDate (datetime.date): The end date of the date range.

        Returns:
            List[Bank1Transaction]: The list of transactions.
        """
        return [
            Bank1Transaction(100.0, Bank1Transaction.TYPE_CREDIT, "Check deposit"),
            Bank1Transaction(25.5, Bank1Transaction.TYPE_DEBIT, "Debit card purchase"),
            Bank1Transaction(225.0, Bank1Transaction.TYPE_DEBIT, "Rent payment"),
        ]

    @property
    def account_balance(self) -> Optional[float]:
        """
        Get the account balance.

        Returns:
            Optional[float]: The account balance.
        """
        return self.getAccountBalance(accountId=0)

    @property
    def account_currency(self) -> Optional[str]:
        """
        Get the account currency.

        Returns:
            Optional[str]: The account currency.
        """
        return self.getAccountCurrency(accountId=0)

    def validateAccountId(self, accountId: int) -> None:
        """
        Validate the account ID.

        Args:
            accountId (int): The account ID.

        Raises:
            ValueError: If the account ID is invalid.
        """
        # Add your account ID validation logic here
        if accountId < 0:
            raise ValueError("Invalid account ID")

    def getValidatedTransactions(
        self, accountId: int, fromDate: datetime.date, toDate: datetime.date
    ) -> List[Bank1Transaction]:
        """
        Get the list of validated transactions for the given account ID and date range.

        Args:
            accountId (int): The account ID.
            fromDate (datetime.date): The start date of the date range.
            toDate (datetime.date): The end date of the date range.

        Returns:
            List[Bank1Transaction]: The list of transactions.

        Raises:
            ValueError: If the account ID is invalid.
        """
        self.validateAccountId(accountId)
        return self.getTransactions(accountId, fromDate, toDate)
