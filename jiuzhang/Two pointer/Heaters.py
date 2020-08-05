
# 双指针+二分答案
def findRadius(houses, heaters):

    houses = sorted(houses)
    heaters=sorted(heaters)

    left = 0
    right = max(len(houses),len(heaters))
    while left + 1< right:
        mid = (left+right) // 2
        # 如果有效，说明当前半径可以满足要求，因此减少
        if is_valid(mid,houses,heaters):
            right = mid
        else:
            left = mid


    if is_valid(left,houses,heaters):
        return left
    return right

def is_valid(r,houses,heaters):
    n = len(heaters)
    m = len(houses)
    now_heater = 0
    for house_pos in houses:
        while now_heater != n and abs(house_pos - heaters[now_heater])>r:
            now_heater += 1
        if now_heater == n:
            return False
    return True

print(findRadius([1,2,3],[2]))




