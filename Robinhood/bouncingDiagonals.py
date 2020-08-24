def bouncingDiagonals(matrix):
    n = len(matrix)
    m=len(matrix[0])
    a,b=0,0
    aa,bb=n-1,0
    hash = {}
    sumOfDiagonalsdown = matrix[0][0]
    sumOfDiagonalsup = matrix[n-1][0]
    result = []
    while a<n-1 and b<m-1:
        first= sumOfDiagonalsdown
        a += 1
        b += 1
        sumOfDiagonalsdown = matrix[a][b] + first
    while aa>0 and bb<m-1:
        second = sumOfDiagonalsup
        aa-=1
        bb+=1
        sumOfDiagonalsup = matrix[aa][bb] + second


    for i in range(n):
        if i == 0:
            hash[matrix[i][0]]=sumOfDiagonalsdown
        elif i == n-1:
            hash[matrix[i][0]] = sumOfDiagonalsup
        else:
            hash[matrix[i][0]]=goup(matrix,i,0)+godown(matrix,0,i)-matrix[0][i]
    sortedhash = sorted(hash.items(),key = lambda item:(item[1],item[0]))
    for item in sortedhash:
        result.append(item[0])
    return result


def goup(matrix,i,j):
    sumOfDiagonals=matrix[i][0]
    while i> 0:
        first = sumOfDiagonals
        i-=1
        j+=1
        sumOfDiagonals = matrix[i][j] + first
    return sumOfDiagonals

def godown(matrix,j, i):
    m = len(matrix[0])
    sumOfDiagonals = matrix[0][i]
    while i < m-1:
        first = sumOfDiagonals
        j += 1
        i += 1
        sumOfDiagonals = matrix[j][i] + first
    return sumOfDiagonals
matrix =[[2, 2, 3], [1, 1, 1], [2, 2, 4]]
print (bouncingDiagonals(matrix))





