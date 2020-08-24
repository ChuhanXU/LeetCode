
#
# 输入是两行。第一行是皇后坐标，第二行是棋子坐标。判断棋子能否被皇后将。是的话打印"Yes"，否则打印“No"。
# 判断一下两个棋子是否在同一行 || 同一列 || 同一对角线。
# 这个题就是判断queen能不能attack到另一个坐标。同一行同一列同一对角线就能attack.判断一下就行
queen = input()
queenIndex = list(map(int,queen.split()))
opponent = input()
opponentIndex = list(map(int,opponent.split()))
def judge(queenIndex,opponentIndex):
    if queenIndex[0]==opponentIndex[0] or opponentIndex[1]==queenIndex[1] or queenIndex[0]-opponentIndex[0] == queenIndex[1] - queenIndex[1]:
        return True
    return False
# queenIndex=[1,1]
# opponentIndex=[1,8]
print(queenIndex,opponentIndex)
print(judge(queenIndex,opponentIndex))



