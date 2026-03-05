# Blockchain_py

A simple Python project to understand **core blockchain and cryptography concepts** by implementing them from scratch.

This project demonstrates how Bitcoin-style addresses are generated using **ECDSA cryptography, hashing, and Base58 encoding**, along with basic blockchain data structures like **Merkle Trees**.

---

# Project Goals

The goal of this repository is educational.
Instead of only using libraries, the code shows **how blockchain fundamentals actually work internally**.

Topics explored:

* Cryptographic key generation
* ECDSA (Elliptic Curve Digital Signature Algorithm)
* SHA-256 hashing
* RIPEMD-160 hashing
* Bitcoin address generation
* QR code generation
* Merkle Tree data structure
* Git project structure and dependency management

---

# Project Structure

```
Blockchain_py
│
├── Blockchain_code/
│
├── Blockchain_data/
│
├── Blockchain_keys.py
├── Markle_tree.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Important Files

**Blockchain_keys.py**

Implements the **Bitcoin wallet generation pipeline**:

```
Private Key
     ↓
ECDSA (secp256k1)
     ↓
Public Key
     ↓
SHA256
     ↓
RIPEMD160
     ↓
Network Byte
     ↓
Checksum
     ↓
Base58 Encoding
     ↓
Bitcoin Address
```

It also generates QR codes for:

* Private Key
* Public Key
* Bitcoin Address

---

**Markle_tree.py**

Implements a basic **Merkle Tree structure** used in blockchains for efficient transaction verification.

Merkle trees allow blockchains to:

* verify transactions quickly
* ensure data integrity
* reduce verification cost

---

# Example Output

```
Private Key (Hex):
7d166191633a8d2b80ed48ee27962482968d1acf4d59f24b1c107ce53f0989f0

Public Key (Hex):
0440a2eac255801c44c2275e88b29675a79406995b95c8fc42c7e36e3a1a57418b32796b229cd33b76cac89c4c833e4767453cf579eab2015ff92cb9417cb2ad28

Bitcoin Address:
1JNDRpNHe9Qd31aQojzuokHCpAeaQjPagx
```

QR codes are generated automatically.

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/blockchain_py.git
cd blockchain_py
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

**Windows**

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Run the Project

Generate keys and Bitcoin address:

```
python Blockchain_keys.py
```

Run Merkle Tree implementation:

```
python Markle_tree.py
```

---

# Dependencies

```
ecdsa
qrcode
pillow
base58
```

These are listed in **requirements.txt**.

---

# Learning Outcomes

By building this project you understand:

* how Bitcoin addresses are derived
* how cryptographic hashing secures blockchain data
* how Merkle Trees verify transactions
* how Python projects are structured professionally
* how Git repositories are managed properly

---

# Future Improvements

Possible extensions:

* digital signature verification
* simple blockchain implementation
* transaction simulation
* CLI wallet generator
* block mining simulation

---

# License

This project is for educational and learning purposes.
