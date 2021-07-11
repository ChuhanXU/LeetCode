
# num 3
# boxes = [1,2,3]
# unitSize = 3
# unitsPerBox = [3,2,1]
# truckSize = 3

# truckSize
def max_units(num,boxes,unitSize,unitsPerBox,truckSize):
    z = list(zip(boxes, unitsPerBox))
    z_sort = sorted(z, key=lambda item: item[1], reverse=True)
    totalUnits=0
    for item in z_sort:
        if truckSize-item[0]>=0:
            totalUnits+=item[0]*item[1]
            truckSize = truckSize-item[0]
        else:
            totalUnits+=truckSize*item[1]

    return totalUnits

print(max_units(3,[1,2,3],3,[3,2,1],3))