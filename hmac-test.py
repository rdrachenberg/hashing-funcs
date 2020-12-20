import hashlib, hmac, binascii

def hmac_sha256(key, msg):
    return hmac.new(key, msg, hashlib.sha256).digest()

key = binascii.unhexlify("fa63f2b4c85af6bed3")
msg = "this is my freaking awesome message".encode("utf8")
print(binascii.hexlify(hmac_sha256(key, msg)))