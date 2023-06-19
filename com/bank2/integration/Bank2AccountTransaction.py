# com/bank2/integration/Bank2AccountTransaction.java
# Created by Par Renyard on 5/12/21.

class Bank2AccountTransaction:
    TRANSACTION_TYPES = {
        "DEBIT": "DEBIT",
        "CREDIT": "CREDIT"
    }

    def __init__(self, amount: float, type: str, text: str) -> None:
        self._amount = amount
        self._type = type
        self._text = text

    def getAmount(self) -> float:
        return self._amount

    def getType(self) -> str:
        return self._type

    def getText(self) -> str:
        return self._text
