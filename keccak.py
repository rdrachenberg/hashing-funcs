from Crypto.Hash import keccak

keccak256 = keccak.new(data=data, digest_bits=256).digest()
print("Keccak256: ", binascii.hexlify(keccak256))
