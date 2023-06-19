# com/bank1/integration/Bank1AccountSource.java
# Created by Par Renyard on 5/12/21.

from typing import List, Optional
import datetime

import os, sys; parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../..')); sys.path.append(parent_dir)
from com.bank1.integration.Bank1Transaction import Bank1Transaction

class Bank1AccountSource:
    def getAccountBalance(self, accountId: int) -> Optional[float]:
        return 215.5

    def getAccountCurrency(self, accountId: int) -> Optional[str]:
        return "USD"

    def getTransactions(
        self, accountId: int, fromDate: datetime.date, toDate: datetime.date
    ) -> List[Bank1Transaction]:

        return [
            Bank1Transaction(100.0, Bank1Transaction.TYPE_CREDIT, "Check deposit"),
            Bank1Transaction(25.5, Bank1Transaction.TYPE_DEBIT, "Debit card purchase"),
            Bank1Transaction(225.0, Bank1Transaction.TYPE_DEBIT, "Rent payment"),
        ]