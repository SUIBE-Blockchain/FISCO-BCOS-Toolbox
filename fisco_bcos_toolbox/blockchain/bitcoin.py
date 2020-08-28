# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import binascii
import secrets
import base58
import ecdsa
import hashlib
from binascii import hexlify, unhexlify

class Bitcoin:

    def ripemd160(s):
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(unhexlify(s))
        return ripemd160.digest()

    @staticmethod
    def generate_addr(priv=None):
        if priv == None:
            # 生成私钥
            bits = secrets.randbits(256)
            # 46518555179467323509970270980993648640987722172281263586388328188640792550961
            bits_hex = hex(bits)
            # 0x66d891b5ed7f51e5044be6a7ebe4e2eae32b960f5aa0883f7cc0ce4fd6921e31
            priv = bits_hex[2:]
            print(len(priv))
            # 66d891b5ed7f51e5044be6a7ebe4e2eae32b960f5aa0883f7cc0ce4fd6921e31
            secret = unhexlify(priv)
            order = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).curve.generator.order()
            p = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).verifying_key.pubkey.point
            x_str = ecdsa.util.number_to_string(p.x(), order)
            y_str = ecdsa.util.number_to_string(p.y(), order)
            compressed = hexlify(bytes(chr(2 + (p.y() & 1)), 'ascii') + x_str).decode('ascii')
            uncompressed = hexlify(bytes(chr(4), 'ascii') + x_str + y_str).decode('ascii')
            hash256FromECDSAPublicKey = hashlib.sha256(binascii.unhexlify(uncompressed)).hexdigest()
            ridemp160FromHash256 = hashlib.new('ripemd160',binascii.unhexlify(hash256FromECDSAPublicKey))
            prependNetworkByte = '00' + ridemp160FromHash256.hexdigest()
            hash = prependNetworkByte
            for x in range(1, 3):
                hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
            cheksum = hash[:8]
            appendChecksum = prependNetworkByte + cheksum
            bitcoinAddress = base58.b58encode(binascii.unhexlify(appendChecksum))
            address =  bitcoinAddress.decode('utf8')
        else:
            secret = unhexlify(priv)
            order = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).curve.generator.order()
            p = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).verifying_key.pubkey.point
            x_str = ecdsa.util.number_to_string(p.x(), order)
            y_str = ecdsa.util.number_to_string(p.y(), order)
            compressed = hexlify(bytes(chr(2 + (p.y() & 1)), 'ascii') + x_str).decode('ascii')
            uncompressed = hexlify(bytes(chr(4), 'ascii') + x_str + y_str).decode('ascii')
            hash256FromECDSAPublicKey = hashlib.sha256(binascii.unhexlify(uncompressed)).hexdigest()
            ridemp160FromHash256 = hashlib.new('ripemd160', binascii.unhexlify(hash256FromECDSAPublicKey))
            prependNetworkByte = '00' + ridemp160FromHash256.hexdigest()
            hash = prependNetworkByte
            for x in range(1, 3):
                hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
            cheksum = hash[:8]
            appendChecksum = prependNetworkByte + cheksum
            bitcoinAddress = base58.b58encode(binascii.unhexlify(appendChecksum))
            address = bitcoinAddress.decode('utf8')

        return {"result": "success",
                "payload":
                {"addr": address,
                 "priv": priv,
                 "pubv": compressed
                 }}


