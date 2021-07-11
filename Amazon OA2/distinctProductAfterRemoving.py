
# input
# num 6
# ids = [1,1,1,2,3,2]
# rem = 2
# output 2
def distinctID(num,ids,rem):
    hash = {}
    for num in ids:
        hash[num]=hash.get(num,0)+1
        #注意sorted返回的是一个list 不是字典
        list = sorted(hash.values())
    size = len(hash)

    for count in list:
        if rem-count>=0:
            size-=1
            rem-=count
        else:
            return size


ids = [1,1,1,2,3,2]
print(distinctID(6,ids,3))