from hashlib import sha256
import datetime

class Block:
    
    def __init__(self, index, previousHash, timestamp, data):
        self.index = index
        self.previousHash = str(previousHash)
        self.timestamp = timestamp
        self.data = data
        self.hash = "empty"

    # 生成されたブロックの情報を出力する
    def printBlockMember(self):
        print(f"--------------------Block{self.index}---------------------")
        print(f"Index: {self.index}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Data: {self.data}")
        print(f"Hash: {self.hash}")
        print(f"PreviousHash: {self.previousHash}")
        print()

    # ブロックのhashをメンバー変数から計算する
    def calcBlockHash(self):
        self.hash = str(sha256((str(self.index) + str(self.timestamp) + self.data + self.previousHash).encode()).hexdigest())

# Block0を生成するための初期値
index = 0
previousHash = 0
timestamp = datetime.datetime.now()
data = "block0data"

# forを0-8で回す
# 各ブロックのタイムスタンプの時差は10秒にしている
# 各ブロックの変数dataはblock[ブロックのindex]というフォーマットにしている
for i in range(9):
    Blocki = Block(index, previousHash, timestamp, data)
    Blocki.calcBlockHash()
    Blocki.printBlockMember()

    # ブロック情報の更新
    index += 1
    timestamp += datetime.timedelta(seconds=10)
    data = f"block{index}data"
    previousHash = Blocki.hash
