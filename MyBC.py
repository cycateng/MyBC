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
#    def calcBlockHash(self):
#        self.hash = str(sha256((str(self.index) + str(self.timestamp) + self.data + self.previousHash).encode()).hexdigest())

# ブロックのハッシュを計算し返す機能
# 引数にBlockのインスタンスを渡す
def calcBlockHash(Block):
    hash = sha256((str(Block.index) + str(Block.timestamp) + Block.data + Block.previousHash).encode()).hexdigest()
    return str(hash)

# 現在のブロックチェーンを出力
def printBlockChain():
    for i in range(9):
        blockList[i].printBlockMember()

# ブロックチェーン検証機能
def checkBlockChain():
    print("Now checking block chain...")
    print()
    print("format")
    print("previousHash:")
    print("hash:")
    print()
    for i in range(9)[::-1]:
        if i == 0:
            break
        
        #対象のブロックの1つ前のブロックのハッシュを計算し
        #対象のブロックのpreviousHashと計算したハッシュを比較する
        preHash = blockList[i].previousHash
        hash = calcBlockHash(blockList[i-1])

        print(f"Block{i}: {preHash}")
        print(f"Block{i-1}: {hash}")
        print()

        if preHash != hash:
            print("ブロックチェーンに矛盾を発見しました")
            print(f"Contradiction: Block{blockList[i].index}'s previousHash and Block{blockList[i-1].index}'s hash")
            print(f"preHash: {preHash}")
            print(f"   hash: {hash}")
            print()

    print("Finish!")

# Blockを格納するlist
blockList = []

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
    Blocki.hash = calcBlockHash(Blocki)
    Blocki.printBlockMember()
    blockList.append(Blocki)

    # ブロック情報の更新
    index += 1
    timestamp += datetime.timedelta(seconds=10)
    data = f"block{index}data"
    previousHash = Blocki.hash

print(blockList)
print()

#print("Block3のhashを改ざん")
#blockList[3].hash = str(sha256("このブロックのハッシュを改ざんしてやったぜ!".encode()).hexdigest())
print("Block6のtimestampを改ざん")
blockList[6].timestamp = datetime.datetime.now()

printBlockChain()
checkBlockChain()
