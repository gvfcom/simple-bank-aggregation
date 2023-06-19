import os, sys; parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../..')); sys.path.append(parent_dir)
import datetime
from com.bank1.integration.Bank1AccountSource import Bank1AccountSource
from com.bank2.integration.Bank2AccountSource import Bank2AccountSource
from BankAdapter import Bank1Adapter, Bank2Adapter

import streamlit as st
import pandas as pd

def get_balances() -> pd.DataFrame():
    """
    Get the account balances from all available bank integrations.
    """
    bank1_account_source = Bank1AccountSource()
    bank2_account_source = Bank2AccountSource()

    # Adapt Bank1AccountSource and Bank2AccountSource to the common AccountSource interface
    adapter1 = Bank1Adapter(bank1_account_source)
    adapter2 = Bank2Adapter(bank2_account_source)

    # Get the balances from all available bank integrations
    balance1 = adapter1.getAccountBalance(accountId=12345)
    currency1 = adapter1.getCurrency(accountId=12345)
    balance2 = adapter2.getAccountBalance(accountId=12345)
    currency2 = adapter2.getCurrency(accountId=12345)

    # Return the balances
    return_dict = {
        "Bank": ["Bank 1", "Bank 2"],
        "Account ID": [12345, 12345],
        "Balance": [balance1, balance2],
        "Currency": [currency1, currency2]
    }
    
    df_return = pd.DataFrame(
        return_dict,
        columns=return_dict.keys()
    )

    return df_return

def get_transactions() -> pd.DataFrame():
    """
    Get the transactions from all available bank integrations.
    """
    bank1_account_source = Bank1AccountSource()
    bank2_account_source = Bank2AccountSource()

    # Adapt Bank1AccountSource and Bank2AccountSource to the common AccountSource interface
    adapter1 = Bank1Adapter(bank1_account_source)
    adapter2 = Bank2Adapter(bank2_account_source)

    # Get the transactions from all available bank integrations
    bank1_transactions = adapter1.getTransactions(
        accountId=12345, from_date=datetime.date(2023, 6, 1), to_date=datetime.date(2023, 6, 30)
    )
    
    return_dict = {
        "Bank": [],
        "Account ID": [],
        "Amount": [],
        "Type": [],
        "Text": []
    }
    for transaction in bank1_transactions:
        return_dict["Bank"].append("Bank 1")
        return_dict["Account ID"].append(12345)
        return_dict["Amount"].append(transaction.getAmount())
        return_dict["Type"].append(transaction.getType())
        return_dict["Text"].append(transaction.getText())

    bank2_transactions = adapter2.getTransactions(
        accountId=12345, from_date=datetime.date(2023, 6, 1), to_date=datetime.date(2023, 6, 30)
    )

    for transaction in bank2_transactions:
        return_dict["Bank"].append("Bank 2")
        return_dict["Account ID"].append(12345)
        return_dict["Amount"].append(transaction.getAmount())
        return_dict["Type"].append(transaction.getType())
        return_dict["Text"].append(transaction.getText())
    
    # Return the balances
    df_return = pd.DataFrame(
        return_dict,
        columns=return_dict.keys()
    )

    return df_return

if __name__ == '__main__':
    st.write("# Simple Bank Aggregation App")
    st.write("## Balances")
    st.table(get_balances())
    st.write("## Transactions")
    st.table(get_transactions())