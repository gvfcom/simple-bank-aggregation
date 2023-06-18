# com/bank2/integration/Bank2AccountTransaction.java
# Created by Par Renyard on 5/12/21.

class Bank2AccountTransaction:
    TRANSACTION_TYPES = {
        "DEBIT": "DEBIT",
        "CREDIT": "CREDIT"
    }

    def __init__(self, amount: float, type: str, text: str) -> None:
        """
        Bank2AccountTransaction constructor.

        Args:
            amount (float): The transaction amount.
            type (str): The transaction type.
            text (str): The transaction text.
        """
        self._amount = amount
        self._type = None
        self.type = type
        self._text = text

    @property
    def amount(self) -> float:
        """
        Get the transaction amount.

        Returns:
            float: The transaction amount.
        """
        return self._amount

    @property
    def type(self) -> str:
        """
        Get the transaction type.

        Returns:
            str: The transaction type.
        """
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        """
        Set the transaction type.

        Args:
            value (str): The transaction type.

        Raises:
            ValueError: If the transaction type is not in the TRANSACTION_TYPES dictionary.
        """
        if value in self.TRANSACTION_TYPES.values():
            self._type = value
        else:
            raise ValueError("Invalid transaction type.")

    @property
    def text(self) -> str:
        """
        Get the transaction text.

        Returns:
            str: The transaction text.
        """
        return self._text
