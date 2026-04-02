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
        return outputs