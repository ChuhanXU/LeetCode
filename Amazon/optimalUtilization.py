
# A = [1, 4, 6, 9], B = [1, 2, 3, 4], K = 9
# return [2, 2]

def optimalUtilization(A,B,K):
    A=sorted(A)
    B=sorted(B)
    result =[]
    max=0
    for i in range(len(A)):
        for j in range(len(B)):
            current =[A[i],B[j]]
            if sum(current)<=K and sum(current)>max:
                result=[i,j]
                max = sum(current)
    return result
A = [1, 4, 6, 9]
B = [1, 2, 3, 4]
print(optimalUtilization(A,B,9))



