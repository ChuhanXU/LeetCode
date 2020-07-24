# 假设如果是递增的应该会 direction>0, currentInt>previousInt, return difference>0(true),
# return difference<0(false)
# 这个题还是有点绕的
# 有两个 corner case 当数组中只有两个值的时候，直接return True
# 当数组中有两个相等的值得时候
def isMonotonic(array):
    if len(array) <= 2:
        return True
    # direction = array[1] - array[0]
    for i in range(len(array)-2):
        direction = array[i+1] - array[i]
        if direction == 0:
            direction = array[i+2] - array[i+1]

        if breaksDirection(direction, array[i+1], array[i+2]):
            return False
    return True


def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0
print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
