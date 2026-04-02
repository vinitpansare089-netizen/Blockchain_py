class UTXO:
    def __init__(self, tx_id, amount, owner):
        self.tx_id = tx_id
        self.amount = amount
        self.owner = owner

    def __repr__(self):
        return f'Coin({self.tx_id}: {self.amount} BTC -> {self.owner})'
    
    def create_transaction(self, receiver, amount_to_send, my_utxos):
        input_utxos = []
        total_input_value = 0

        for coin in my_utxos:
            input_utxos.append(coin)
            total_input_value += coin.amount
            if total_input_value >= amount_to_send:
                break

        if total_input_value < amount_to_send:
            return "Insufficient funds!"
        
        outputs = []
        outputs.append(UTXO('TX99_A', amount_to_send, receiver))

        change = total_input_value - amount_to_send
        if change > 0:
            outputs.append(UTXO('TX99_B', change, self.owner))

        return {
            "spent_ids": [coin.tx_id for coin in input_utxos],
            "new_utxos": outputs
        }

# Wallet
wallet = [UTXO('TX01', 5, 'Alice'), UTXO('TX02', 3, 'Alice')]

print(f"Alice's wallet: {wallet}")

tx = wallet[0].create_transaction("Bob", 6, wallet)

print(f"\nTransaction processed:")
print(f"Spent UTXOs: {tx['spent_ids']}")
print(f"New UTXOs: {tx['new_utxos']}")