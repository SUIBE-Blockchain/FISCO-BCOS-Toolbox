# -*- coding:utf8 -*-
from web3 import Web3
from eth_account import Account

class Ethereum:
    @staticmethod
    def generate_addr(priv=None):
        if priv == None:
            account = Account.create()
        else:
            try:
                account = Account.privateKeyToAccount(priv)
            except:
                return {"result": "error"}
        return {"result":"success",
        "payload":
        {"addr": account.address, 
        "priv": account.privateKey.hex()}}