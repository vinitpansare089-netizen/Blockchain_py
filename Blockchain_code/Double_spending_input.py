class Blockchain:
    def __init__(self):
        self.balance = 100
        self.pending_transactions = []

    def create_transaction(self, amount, recipient):
        if amount <= self.balance:
            self.pending_transactions.append({"amount": amount, "to": recipient})
            print(f"Transaction of {amount} to {recipient} added to mempool.")
            return True
        else:
            print("Inadequate funds")
            return False
        
    def mine(self):
        total_spent = sum(tx["amount"] for tx in self.pending_transactions)

        if total_spent > self.balance:
            print("❌ Double spending attempt detected!")
            print(f'Attempted: {total_spent}, Available: {self.balance}')
        else:
            self.balance -= total_spent
            print(f"✅ Transactions mined! Remaining balance: {self.balance}")
            self.pending_transactions = []


# MAIN
wallet = Blockchain()

print(f"Current Balance: {wallet.balance}")

amount = int(input("Enter amount to send: "))

wallet.create_transaction(amount, "Alice")

print("\nAttempting to double spend...")
wallet.create_transaction(amount, "Bob")

wallet.mine()