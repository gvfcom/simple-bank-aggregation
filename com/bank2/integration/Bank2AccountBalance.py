# com/bank2/integration/Bank2AccountBalance.java
# Created by Par Renyard on 5/12/21.

class Bank2AccountBalance:
    def __init__(self, balance: float, currency: str) -> None:
        self._balance = balance
        self._currency = currency

    def getBalance(self) -> float:
        return self._balance

    def getCurrency(self) -> str:
        return self._currency
