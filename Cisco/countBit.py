# 统计一个整数的二进制式里有多少个1

def countBit(n):
    count = 0
    while n:
        n &= (n-1)
        count += 1
    return(count)
print(countBit(10))
# 10 1010 2
# 10 &= 9  1010 &= 1001 = 1000