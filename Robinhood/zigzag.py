def zigzag(numbers):
    n = len(numbers)
    if n == 0:
        return 0
    ans = [0] * (n - 2)
    for i in range(n - 2):
        if ((numbers[i+1] > numbers[i] and numbers[i+1] > numbers[i+2]) or (numbers[i+1] < numbers[i] and numbers[i+1] < numbers[i+2])):
            ans[i]=1
    return ans


numbers = []
print(zigzag(numbers))
