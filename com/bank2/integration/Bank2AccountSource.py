# com/bank2/integration/Bank2AccountSource.java
# Created by Par Renyard on 5/12/21.

from typing import List
import datetime

from com.bank2.integration.Bank2AccountBalance import Bank2AccountBalance
from com.bank2.integration.Bank2AccountTransaction import Bank2AccountTransaction

class Bank2AccountSource:
    @property
    def balance(self) -> Bank2AccountBalance:
        """
        Get the account balance for the given account number.

        Returns:
            Bank2AccountBalance: The account balance.
        """
        return Bank2AccountBalance(512.5, "USD")

    @property
    def transactions(self) -> List[Bank2AccountTransaction]:
        """
        Get the list of transactions for the given account number and date range.

        Returns:
            List[Bank2AccountTransaction]: The list of transactions.
        """
        return [
            Bank2AccountTransaction(125.0, Bank2AccountTransaction.TRANSACTION_TYPES["DEBIT"], "Amazon.com"),
            Bank2AccountTransaction(500.0, Bank2AccountTransaction.TRANSACTION_TYPES["DEBIT"], "Car insurance"),
            Bank2AccountTransaction(800.0, Bank2AccountTransaction.TRANSACTION_TYPES["CREDIT"], "Salary"),
        ]
