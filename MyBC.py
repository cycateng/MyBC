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
    for i in blockList:
        i.printBlockMember()

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

# main関数
def main():
    index = 0
    previousHash = 0
    timestamp = datetime.datetime.now()
    data = "initial data"

    j = 7
    for i in range(100):
        Blocki = Block(index, previousHash, timestamp, data)
        Blocki.hash = calcBlockHash(Blocki)
        #Blocki.printBlockMember()
        blockList.append(Blocki)

        index += 1
        path = f"logs/system.log.{j}.gz"
        try:
            f = open(path,'rb')
        except FileNotFoundError:
            #print("これ以上ログファイルが存在しません")
            BLocki = Block(index, previousHash, timestamp, data)
            Blocki.hash = calcBlockHash(Blocki)
            blockList.append(Blocki)
            break
            
        #timestamp += datetime.timedelta(seconds=10)
        timestamp = datetime.datetime.fromtimestamp(os.stat(path).st_mtime)
        #data = f"block{index}data"
        data = sha256(f.read()).hexdigest()
        previousHash = Blocki.hash
        f.close()
        j -= 1
    
    printBlockChain()
    '''
    print(blockList)
    print()
    print("Block6のtimestampを改ざん")
    blockList[6].timestamp = datetime.datetime.now()
    printBlockChain()
    checkBlockChain()
    '''

blockList = []
if __name__ == '__main__':
    main()
