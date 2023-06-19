import os, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../..')); sys.path.append(parent_dir)
from com.bank1.integration.Bank1Transaction import Bank1Transaction
from com.bank2.integration.Bank2AccountTransaction import Bank2AccountTransaction

class BankTransactionAdapter:
    """
    Adapter class for bank transactions.
    """

    TRANSACTION_TYPES = {
        "DEBIT": "DEBIT",
        "CREDIT": "CREDIT"
    }

    def getAmount(self) -> float:
        """
        Get the transaction amount.

        Returns:
            float: The transaction amount.
        """
        raise NotImplementedError()

    def getType(self) -> str:
        """
        Get the transaction type.

        Returns:
            str: The transaction type.
        """
        raise NotImplementedError()

    def getText(self) -> str:
        """
        Get the transaction text.

        Returns:
            str: The transaction text.
        """
        raise NotImplementedError()

class Bank1TransactionAdapter(BankTransactionAdapter):
    """
    Adapter class for Bank1Transaction.
    """

    TRANSACTION_TYPES = {
        1: "CREDIT",
        2: "DEBIT"
    }

    def __init__(self, bank1_transaction: Bank1Transaction):
        self.bank1_transaction = bank1_transaction

    def getAmount(self) -> float:
        """
        Get the transaction amount.

        Returns:
            float: The transaction amount.
        """
        return self.bank1_transaction.getAmount()

    def getType(self) -> str:
        """
        Get the transaction type.

        Returns:
            str: The transaction type.
        """
        if self.bank1_transaction.getType() in self.TRANSACTION_TYPES.keys():
            return super().TRANSACTION_TYPES[
                self.TRANSACTION_TYPES[
                    self.bank1_transaction.getType()
                ]
            ]
        else:
            raise ValueError()

    def getText(self) -> str:
        """
        Get the transaction text.

        Returns:
            str: The transaction text.
        """
        return self.bank1_transaction.getText()


class Bank2TransactionAdapter(BankTransactionAdapter):
    """
    Adapter class for Bank2AccountTransaction.
    """

    TRANSACTION_TYPES = {
        "DEBIT": "DEBIT",
        "CREDIT": "CREDIT"
    }

    def __init__(self, bank2_transaction: Bank2AccountTransaction):
        self.bank2_transaction = bank2_transaction

    def getAmount(self) -> float:
        """
        Get the transaction amount.

        Returns:
            float: The transaction amount.
        """
        return self.bank2_transaction.getAmount()

    def getType(self) -> str:
        """
        Get the transaction type.

        Returns:
            str: The transaction type.
        """
        if self.bank2_transaction.getType() in self.TRANSACTION_TYPES.keys():
            return super().TRANSACTION_TYPES[
                self.TRANSACTION_TYPES[
                    self.bank2_transaction.getType()
                ]
            ]
        else:
            raise ValueError()

    def getText(self) -> str:
        """
        Get the transaction text.

        Returns:
            str: The transaction text.
        """
        return self.bank2_transaction.getText()