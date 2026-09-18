# decrypt data xor and return string data
def xor_de_en(text_crypt: bytes, key: bytes) -> bytes:
    return bytes((b ^ key[i % len(key)]) for i, b in enumerate(text_crypt))