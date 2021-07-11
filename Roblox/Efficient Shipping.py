def max_units(boxes,unitPerBox,truckSize):
    n = len(boxes)
    dp= [0] * (len(boxes)+1)

    for i in range(n):
        for j in range(truckSize,0,-1):
            dp[j]=max(dp[j],dp[j-boxes[i]]+boxes[i]*unitPerBox[i])

    return dp[truckSize]

boxes = [1,2,3]
unitPerBox = [3,2,1]
truckSize = 3;
print (max_units(boxes,unitPerBox,truckSize))
