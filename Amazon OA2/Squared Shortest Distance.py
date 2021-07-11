
def shortestDistance(num,positionX,positionY):
    result = float('inf')
    for i in range(num-1):
        for j in range(i+1,num):
            distance = ((positionX[j]-positionX[i])*(positionX[j]-positionX[i]))+((positionY[j]-positionY[i])*(positionY[j]-positionY[i]))
            if distance>0:
                result = min(distance,result)
    return result
num=3
positionX=[0,1,2]
positionY=[0,1,4]
print(shortestDistance(num,positionX,positionY))