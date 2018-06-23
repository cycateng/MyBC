from hashlib import sha256
import datetime
import os

# Block Class
class Block:
    
    def __init__(self, index, previousHash, timestamp, data):
        self.index = index
        self.previousHash = str(previousHash)
        self.timestamp = timestamp
        self.data = data
        self.hash = "empty"

    # ブロックの情報を出力する機能
    def printBlockMember(self):
        print(f"--------------------Block{self.index}---------------------")
        print(f"Index: {self.index}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Data: {self.data}")
        print(f"Hash: {self.hash}")
        print(f"PreviousHash: {self.previousHash}")
        print()

# ブロックのハッシュを計算し返す機能
# 引数にBlockのインスタンスを渡す
def calcBlockHash(Block):
    hash = sha256((str(Block.index) + str(Block.timestamp) + Block.data + Block.previousHash).encode()).hexdigest()
    return str(hash)

# 現在のブロックチェーンを出力
def printBlockChain():
    for block in blockList:
        block.printBlockMember()

# ブロックチェーン検証機能
def checkBlockChain():
    print("Now checking block chain...")
    print()
    print("format")
    print("previousHash:")
    print("hash:")
    print()
    for i in range(len(blockList))[::-1]:
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

# main関数
def main():
    print("Genesis block created")
    index = 0
    previousHash = 0
    timestamp = datetime.datetime.now()
    data = "This is Genesis Block!"

    logs = os.listdir('logs/')
    logs.reverse()
    for path in logs:
        Blockindex = Block(index, previousHash, timestamp, data)
        Blockindex.hash = calcBlockHash(Blockindex)
        #Blocki.printBlockMember()
        blockList.append(Blockindex)

        try:
            f = open(f"logs/{path}",'rb')
        except IOError:
            print("ファイルが開けません")
        except FileNotFoundError:
            print("ログファイルが存在しません")
            
        #timestamp += datetime.timedelta(seconds=10)
        timestamp = datetime.datetime.fromtimestamp(os.stat(f"logs/{path}").st_mtime)
        #data = f"block{index}data"
        data = sha256(f.read()).hexdigest()
        previousHash = Blockindex.hash
        index += 1
        f.close()
    
    printBlockChain()
    checkBlockChain()

blockList = []
if __name__ == '__main__':
    main()
