#!/usr/bin/env python
# - * - coding: utf - 8 -
# 2019.12.28 update gm config
import os
from eth_utils.crypto import set_crypto_type, CRYPTO_TYPE_GM, CRYPTO_TYPE_ECDSA


class client_config:
    """
    类成员常量和变量，便于用.调用和区分命名空间
    """
    # keyword used to represent the RPC Protocol
    PROTOCOL_RPC = "rpc"
    # keyword used to represent the Channel Protocol
    PROTOCOL_CHANNEL = "channel"

    # ---------crypto_type config--------------
    # crypto_type : 大小写不敏感："GM" for 国密, "ECDSA" 或其他是椭圆曲线默认实现。
    crypto_type = "GM"
    crypto_type = crypto_type.upper()
    set_crypto_type(crypto_type)  # 使密码算法模式全局生效，切勿删除此行

    # --------------------------------------
    # configure below
    # ---------client communication config--------------
    client_protocol = "88888888888"  # or PROTOCOL_CHANNEL to use channel prototol
    # client_protocol = PROTOCOL_CHANNEL
    remote_rpcurl = "http://127.0.0.1:8545"  # 采用rpc通信时，节点的rpc端口,和要通信的节点*必须*一致,如采用channel协议通信，这里可以留空
    channel_host = "127.0.0.1"  # 采用channel通信时，节点的channel ip地址,如采用rpc协议通信，这里可以留空
    channel_port = 20200  # 节点的channel 端口,如采用rpc协议通信，这里可以留空
    channel_ca = "bin/ca.crt"  # 采用channel协议时，需要设置链证书,如采用rpc协议通信，这里可以留空
    channel_node_cert = "bin/sdk.crt"  # 采用channel协议时，需要设置sdk证书,如采用rpc协议通信，这里可以留空
    channel_node_key = "bin/sdk.key"  # 采用channel协议时，需要设置sdk私钥,如采用rpc协议通信，这里可以留空
    fiscoChainId = 1  # 链ID，和要通信的节点*必须*一致
    groupid = 1  # 群组ID，和要通信的节点*必须*一致，如和其他群组通信，修改这一项，或者设置bcosclient.py里对应的成员变量

    # ---------account &keyfile config--------------
    # 注意账号部分，国密和ECDSA采用不同的配置
    contract_info_file = "bin/contract.ini"  # 保存已部署合约信息的文件
    account_keyfile_path = "bin/accounts"  # 保存keystore文件的路径，在此路径下,keystore文件以 [name].keystore命名
    account_keyfile = "pyaccount.keystore"
    account_password = "123456"  # 实际使用时建议改为复杂密码
    gm_account_keyfile = "gm_account.json"  # 国密账号的存储文件，可以加密存储,如果留空则不加载gm_account_password = "123456"
    gm_account_password = "123456"
    # ---------console mode, support user input--------------
    background = True

    # ---------runtime related--------------
    # path of solc compiler
    solc_path = "./bin/solc.exe"
    gm_solc_path = "./bin/solc/v0.4.25/solc-gm"
    solcjs_path = "./solc.js"

    logdir = "bin/logs"  # 默认日志输出目录，该目录必须先建立