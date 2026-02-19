import hashlib
import time

def create_block_hash(data,previous_hash):
  timestamp= time.time()

  block_content = str(timestamp) + data + previous_hash
  hash_key = hashlib.sha256(block_content.encode())
  return hash_key.hexdigest()

  print("--Creating PREVIOUS BLOCK (Genesis)--")
  data_prev = input("Enter data for previous block: ")
  hash_prev = create_block_hash(data_prev, "0")
  next_pointer_prev = "Middle Block"


# --- 2. THE MIDDLE BLOCK ---

  print("\n---Creating MIDDLE BLOCK---")
  data_mid = input("Enter data for middle block: ")
  hash_mid = create_block_hash(data_mid, hash_prev)
  next_pointer_mid = "Next Block"

#--- 3. THE NEXT BLOCK (Tail Node) ---
  print("\n--- Creating NEXT BLOCK (Tail) ---")
  data_next = input("Enter data for Next Block: ")
  hash_next = create_block_hash(data_next, hash_mid)
  next_pointer_next = "NULL"

#---Final Display ---
  print("\n" + "="*50)
  print("BLOCKCHAIN SUMMARY")
  print("="*50)

  blocks = [
    ("PREVIOUS", data_prev, "0", hash_prev, next_pointer_prev),
    ("MIDDLE", data_mid, hash_prev, hash_mid, next_pointer_mid),
    ("NEXT", data_next, hash_mid, hash_next, next_pointer_next)
  ]

  for name, data, prev, curr, nxt in blocks:
    print(f"[{name} BLOCK]")
    print(f" Data:  {data}]")
    print(f"prev_hash: {prev[:15]}...")
    print(f"curr Hash: {curr[:15]}...")
    print(f"pointer:  {nxt}")
    print("-" * 30)

