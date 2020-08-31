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
        "priv": account.privateKey.hex(),
        "pubv": str(account._key_obj.public_key)
         }}
    
    @staticmethod
    def split_sig(sig):
        try:
            r = sig[:66]
            s = "0x" + sig[66:130]
            v = int(sig[130:],16)
            return {"result": "success",
            "payload": {"r": r, "s": s, "v": v}}
        except:
            return {"result": "error"}