# def findPrimeON(arr):
#     gmax = max(arr)
#     prime=[]
#     SPF= [None]* (gmax+1)
#     isPrime= [True]*(gmax+1)
#     for i in range(2,gmax+1):
#         if isPrime[i] == True:
#             prime.append(i)
#             SPF[i] = i
#         j = 0
#         while j < len(prime) and i* prime[j]<gmax and prime[j]<= SPF[i]:
#             isPrime[i*prime[j]]= False
#             SPF[i* prime[j]] =prime[j]
#             j+= 1
#     return prime
# arr=[10,11,12,41,21,2]
# print(findPrimeON(arr))
# def countPrimes(n):
#     if n <= 2:
#         return 0
#     res = [True] * n
#     res[0] = res[1] = False
#     for i in range(2, n):
#         if res[i] == True:
#             for j in range(2, (n-1)//i+1):
#                 res[i*j] = False
#     return sum(res)
# print(countPrimes(2))
def findPrimeON(arr):
    result = [''for i in range(len(arr))]

    for i in range(len(arr)):
       if isPrime(arr[i]):
           result[i] = "prime"
       else:
           result[i] = "com"
    return result


def isPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True


arr=[2,5,6,7]
print(findPrimeON(arr))







