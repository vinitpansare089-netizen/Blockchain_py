#VINIT PANSARE
import os
import hashlib
import ecdsa
import qrcode
import base58

# Generate Private Key...first vinit
private_key = os.urandom(32)
private_key_hex = private_key.hex()

#private key bhi Bhai
print("Private Key (Hex):")
print(private_key_hex)

# Generate Public Key using ECDSA
sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()

public_key = b'\x04' + vk.to_string()
public_key_hex = public_key.hex()

print("\nPublic Key (Hex):")
print(public_key_hex)

# SHA256
sha256_bpk = hashlib.sha256(public_key).digest()

# RIPEMD160
ripemd160_bpk = hashlib.new('ripemd160', sha256_bpk).digest()

#  Add network byte 
network_byte = b'\x00'
network_bitcoin_public_key = network_byte + ripemd160_bpk

# Double SHA256 for checksum
sha256_1 = hashlib.sha256(network_bitcoin_public_key).digest()
sha256_2 = hashlib.sha256(sha256_1).digest()

checksum = sha256_2[:4]

# Append checksum
address_bytes = network_bitcoin_public_key + checksum

# Base58 Encoding to Bitcoin Address
bitcoin_address = base58.b58encode(address_bytes)

print("\nBitcoin Address:")
print(bitcoin_address.decode())

#Generate QR Codes...ok vinit.........
private_qr = qrcode.make(private_key_hex)
private_qr.save("private_key_qr.png")

public_qr = qrcode.make(public_key_hex)
public_qr.save("public_key_qr.png")

address_qr = qrcode.make(bitcoin_address.decode())
address_qr.save("bitcoin_address_qr.png")

print("\nQR Codes Generated Successfully!")
print("Files saved as:")
print("private_key_qr.png")
print("public_key_qr.png")
print("bitcoin_address_qr.png")