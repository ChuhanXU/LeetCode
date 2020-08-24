# 第三题题目忘记截了，
# 大致就 '.' 代表空格， '#' 代表方块， '*' 代表obstacle
# 然后给你一个mxn matrix
# 你clockwise rotate成nxm，
# 并且所有方块顺重力往下掉，除非碰到别的方块/obstacle/bottom
def rotateAndFall(box):
    m,n = len(box),len(box[0])
    for i in range(m):
        moving = True
        while moving:
            moving = False
            for j in range(n-1,-1,-1):
                if box[i][j]=='.' or box[i][j]=='*' or j==n-1:
                    continue
                if box[i][j+1]=='.':
                    moving = True
                    box[i][j+1] = '#'
                    box[i][j]='.'
    rotated = [[box[m-1-j][i] for j in range(m)]for i in range(n)]
    return rotated