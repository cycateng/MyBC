from hashlib import sha256
from datetime import datetime

class Block:
    
    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = index
        self.previousHash = str(previousHash)
        self.timestamp = timestamp
        self.data = data
        self.hash = str(hash)

def calculateHash(Block):
    pass

index = 0
initialHash = sha256(b"this is initial hash").hexdigest()
timestamp = datetime.now()
data = "block0data"
previousHash = 0
print("--------------------Block0---------------------")
print(f"Index: {index}")
print(f"Timestamp: {timestamp}")
print(f"Data: {data}")
print(f"Hash: {initialHash}")
print(f"PreviousHash: {previousHash}")
