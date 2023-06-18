# com/pyyne/challenge/bank/BankController.java

from com.bank1.integration.Bank1AccountSource import Bank1AccountSource
from com.bank2.integration.Bank2AccountSource import Bank2AccountSource

# Controller that pulls information form multiple bank integrations and prints them to the console.
# Created by Par Renyard on 5/12/21.

class BankController:
    def printBalances(self) -> None:
        """
        Print balance information from all available bank integrations.
        """
        print("Implement me to pull balance information from all available bank integrations and display them, one after the other.")

    def printTransactions(self) -> None:
        """
        Print transactions from all available bank integrations.
        """
        print("Implement me to pull transactions from all available bank integrations and display them, one after the other.")