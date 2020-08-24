def movingDiagonals(n,m,x1,y1,x2,y2):
    if n == 0:
        return -1
    if m == 0:
        return -1
    delta_x = 1
    delta_y = 1
    newX = x1
    newY = y1
    ans = 0
    while newX!=x2 or newY!=y2:

        newX = newX+delta_x
        newY = newY+delta_y

        if newX == n:
            newX = newX - delta_x
            newY = newY - delta_y
            delta_x = -1

        if newY == m:
            newX = newX - delta_x
            newY = newY - delta_y
            delta_y = -1
        if newX==x1 and newY==y1 and delta_x==x1 and delta_x==y1:
            return -1
        ans += 1
    return ans
print(movingDiagonals(5,5,2,1,1,2))
