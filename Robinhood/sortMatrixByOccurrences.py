
#first sort its values in ascending order of how frequently the number occurs in m
# in the case of a tie, sort the equally frequent numbers by their values,in ascending order
# place the sorted numbers diagonally, starting from the bottom right corner
# input {{2, 2, 3, 4}, {1, 1, 1, 3}, {2, 2, 4, 4}, {2, 1, 2, 5}}
# output {{2, 2, 2, 1}, {2, 2, 1, 4}, {2, 1, 4, 3}, {1, 4, 3, 5}}
# using hashtable to store the occurrences of every number in m
# sorted them by occurrences and values
# fill this m from right bottom corner
import math
import numpy as np


def sortMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    hash = {}
    # hashList = []
    for i in range(n):
        for j in range(m):
            hash[matrix[i][j]]=hash.get(matrix[i][j],0)+1

    sortedHash = sorted(hash.items(),key = lambda item:(item[1],item[0]))
    print(sortedHash)
    result = []
    for item in sortedHash:
        frequency = item[1]
        while frequency>0:
            result.append(item[0])
            frequency-=1
    return putElement(n,m,result)
    # for key,value in sortedHash.items():
    #     temp = [key,value]
    #     hashList.append(temp)
# 2 2 1
# 2 1 5
# 1 4 3
def putElement(n,m,array):
    a=0
    matrix = [[0] * m for i in range(n)]
    for sum in range(2*(n-1),-1,-1):
        for i in range(min(sum,n-1),-1,-1):
            j = sum-i
            if j>=m:
                break
            matrix[i][j] = array[a]
            a+=1
    return matrix
matrix = [[2, 2, 3, 4], [1, 1, 1,3], [2, 2, 4,4],[1,2,2,5]]
print(sortMatrix(matrix))


















    # how to fill matrix from bottom right corner
    # frequency = 0
    # index = -1
    # # 每一条对角线上的横纵坐标加起来相等
    # for sum in range(2*(n-1),-1,-1):
    #     for i in range(min(n-1,sum),-1,-1):
    #         j = sum -i
    #         if j>=m:
    #             continue
    #         if frequency==0:
    #             index+=1
    #             frequency = sortedHash[index][1]
    #         result[i][j]=sortedHash[index][0]
    #         frequency-=1
    # return result

# matrix = [[2, 2, 3], [1, 1, 1], [5, 2, 4]]
# print(sortMatrix(matrix))



    # while(n-1)>=0 and (m-1)>=0:
    #     for i in len(sortedHash):
    #         j = sortedHash[i].value
    #         while j>0:
    #             result[n-1][m-1] = sortedHash[i].key
    #             j-=1

