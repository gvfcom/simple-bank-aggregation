# com/bank1/integration/Bank1Transaction.java
# Created by Par Renyard on 5/12/21.

class Bank1Transaction:
    TYPE_CREDIT: int = 1
    TYPE_DEBIT: int = 2

    def __init__(self, amount: float, type: int, text: str) -> None:
        self._amount = amount
        self._type = type
        self._text = text

    def getAmount(self) -> float:
        return self._amount

    def getType(self) -> int:
        return self._type

    def getText(self) -> str:
        return self._text