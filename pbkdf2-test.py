import os, binascii
from backports.pbkdf2 import pbkdf2_hmac

salt = os.urandom(32)
passwd = "thisIsAnAwesomePassword".encode("utf8")
key = pbkdf2_hmac("sha256", passwd, salt, 500000, 32)
print("derived key:", binascii.hexlify(key))