# com/bank1/integration/Bank1Transaction.java
# Created by Par Renyard on 5/12/21.

class Bank1Transaction:
    TYPE_CREDIT: int = 1
    TYPE_DEBIT: int = 2

    def __init__(self, amount: float, type: int, text: str) -> None:
        """
        Bank1Transaction constructor.

        Args:
            amount (float): The transaction amount.
            type (int): The transaction type.
            text (str): The transaction text.
        """
        self._amount = amount
        self._type = type
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
    def type(self) -> int:
        """
        Get the transaction type.

        Returns:
            int: The transaction type.
        """
        return self._type

    @type.setter
    def type(self, value: int) -> None:
        """
        Set the transaction type.

        Args:
            value (int): The transaction type.

        Raises:
            ValueError: If the transaction type is not valid.
        """
        if value not in (Bank1Transaction.TYPE_CREDIT, Bank1Transaction.TYPE_DEBIT):
            raise ValueError("Invalid transaction type")
        self._type = value

    @property
    def text(self) -> str:
        """
        Get the transaction text.

        Returns:
            str: The transaction text.
        """
        return self._text
