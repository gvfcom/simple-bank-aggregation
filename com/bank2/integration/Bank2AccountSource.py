# com/bank2/integration/Bank2AccountSource.java
# Created by Par Renyard on 5/12/21.

import os, sys; parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../..')); sys.path.append(parent_dir)
from com.bank2.integration.Bank2AccountBalance import Bank2AccountBalance

from typing import List
import datetime

import os, sys; parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../..')); sys.path.append(parent_dir)
from com.bank2.integration.Bank2AccountBalance import Bank2AccountBalance
from com.bank2.integration.Bank2AccountTransaction import Bank2AccountTransaction

class Bank2AccountSource:
    def getBalance(self, accountNum: int) -> Bank2AccountBalance:
        return Bank2AccountBalance(512.5, "USD")

    def getTransactions(self, accountNum: int, fromDate: datetime.date, toDate: datetime.date) -> List[Bank2AccountTransaction]:
        return [
            Bank2AccountTransaction(125.0, Bank2AccountTransaction.TRANSACTION_TYPES["DEBIT"], "Amazon.com"),
            Bank2AccountTransaction(500.0, Bank2AccountTransaction.TRANSACTION_TYPES["DEBIT"], "Car insurance"),
            Bank2AccountTransaction(800.0, Bank2AccountTransaction.TRANSACTION_TYPES["CREDIT"], "Salary"),
        ]