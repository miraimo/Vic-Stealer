"""This module provides functions for encrypting and decrypting data using the XOR cipher. The XOR cipher is a simple symmetric encryption technique that applies the bitwise XOR operation between the data and a repeating key."""

# decrypt data xor and return string data
def xor_de_en(text_crypt: bytes, key: bytes) -> bytes:
    return bytes((b ^ key[i % len(key)]) for i, b in enumerate(text_crypt))