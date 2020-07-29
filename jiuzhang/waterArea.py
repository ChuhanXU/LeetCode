def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i]=leftMax
        leftMax = max(leftMax,height)
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        # 这个时候的maxes[i]就是对应的左边最大pillar
        minHeight = min(rightMax,maxes[i])
        if height < minHeight:
            maxes[i]=minHeight - height
        else:
            maxes[i]=0
        #     在更换rightMax的值，可以用一个数组完成三个数组的事情，1，当前位置的左边最大pillars，2，当前位置的右边最大pillar 3，当前位置左右pillars的较小的那个pillar减去height
        rightMax = max(rightMax,height)
    return sum(maxes)
print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))