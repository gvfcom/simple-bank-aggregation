# com/bank2/integration/Bank2AccountBalance.java
# Created by Par Renyard on 5/12/21.

class Bank2AccountBalance:
    def __init__(self, balance: float, currency: str) -> None:
        """
        Bank2AccountBalance constructor.

        Args:
            balance (float): The account balance amount.
            currency (str): The currency of the account balance.
        """
        self._balance = balance
        self._currency = currency

    @property
    def balance(self) -> float:
        """
        Get the account balance.

        Returns:
            float: The account balance.
        """
        return self._balance

    @property
    def currency(self) -> str:
        """
        Get the account currency.

        Returns:
            str: The account currency.
        """
        return self._currency
