def zigzag(numbers):
    n = len(numbers)
    if n == 0:
        return 0

    result = zigzag(helper(numbers))
    return result

def helper(numbers):
    n = len(numbers)
    if n == 0:
        return 0
    ans = [0] * (n)
    for i in range(1,n):
        if numbers[i]>numbers[i-1] and numbers[i]>numbers[i+1]:
            ans[i]=1
    m = len(ans)
    result=[]
    for i in range(m):
        if ans[i]==1:
            result.append(numbers[i])
    h = min(result)
    numbers.remove(h)
    return numbers


numbers = [2,7,8,5,1,6,3,9,4]
print(zigzag(numbers))
