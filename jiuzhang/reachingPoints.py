# Basic idea:
# If we start from sx,sy, it will be hard to find tx, ty.
# If we start from tx,ty, we can find only one path to go back to sx, sy.
# I cut down one by one at first and I got TLE. So I came up with remainder.
#
# First line:
# if 2 target points are still bigger than 2 starting point, we reduce target points.
# Second line:
# check if we reduce target points to (x, y+kx) or (x+ky, y)
#
# Time complexity
# I will say O(logN) where N = max(tx,ty).
def reachingPoints(sx,sy,tx,ty):
    while sx< tx and sy < ty:
        tx,ty = tx%ty,ty%tx
    return sx == tx and sy<=ty and (ty-sy)%sx == 0 or sy == ty and sx <= tx and (tx-sx) % sy == 0
# 第一种情况是 while循环后 x的起点和终点相等，y的起点和终点不等，并且y的终点要大于起点，改变y的唯一途径是加x的倍数，所以我们要判断y的终点和起点的差等不等于起点x的倍数
print(reachingPoints(1,1,5,2))

