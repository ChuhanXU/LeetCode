def orderCheck(height):
    count = 0
    heightSorted = sorted(height)
    for i in range(len(height)):

        if height[i] == heightSorted[i]:
            continue
        else:
            count += 1
    return count

print(orderCheck([4,3,2,1]))


