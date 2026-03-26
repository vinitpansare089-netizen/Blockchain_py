import hashlib
import time

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        
class Blockchain:
    def __init__(self):
        self.balances = {"vivek": 100, "vinit": 100, "rohit": 100}
        self.chain = []
        self.pending_transactions = []

    def add_transaction(self, transaction):
        if self.balances[transaction.sender] >= transaction.amount:
           self.balances[transaction.sender] -= transaction.amount
           self.pending_transactions.append(transaction)
           print(f'Transaction added: {transaction.sender} -> {transaction.receiver} : {transaction.amount}')
           return True
        else:
            print(f'Failed: Double Spend Attempt by {transaction.sender}')  
            return False