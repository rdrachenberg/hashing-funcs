import pyaes, pbkdf2, binascii, os, secrets

plaintext = "Here is my super secret message!"
password = "ThisIsAnAwesomePassword"
key = pbkdf2.PBKDF2(password, 'some salt').read(16)
print('AES encryption key:', binascii.hexlify(key))

iv = secrets.randbelow(2 << 128)
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('encrypted:', binascii.hexlify(ciphertext))

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)
print('decrypted: ', decrypted)