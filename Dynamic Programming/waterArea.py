
# how to find the height of tallest pillar to the left:
# 1.iterate from the first value and record every height
# 2.initialize the max array and leftMax,because the leftmax of the first value will be 0
# 3.update the leftMax by comparing with every height and got the bigger one
# 4.if we want to use one array to replace three array,we can adjust our order of operation,because you know we already konw that the rightmax value of
# the final index in the input array is 0, there is nothing after the final index.
# 5.we can calculate the amount of water at the final index first and then update our rightmax array
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
# leftmax       [0, 0, 8, 8, 8, 8, 8, 8, 10,10,10,10,3,0]
# water         [                                       ,0 ]