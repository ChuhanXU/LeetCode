
# 输入一个数字n，返回一个w，b相间的棋子板，第一个必须是w
n = int(input())
def WB(n):
    chessBoard = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            chessBoard[i][j]=(i+j)%2
            if chessBoard[i][j]== 0:
                chessBoard[i][j]= "W"
            else:
                chessBoard[i][j]= "B"

    return chessBoard
print(WB(n))


