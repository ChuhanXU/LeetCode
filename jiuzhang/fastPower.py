# time O(logn)
def fastPower(a,b,n):
    if b == 1:
        return 0
    if n == 0:
        return 1
    # 按奇数偶数分类，奇数要单独乘一个a
    if n % 2 == 1:
        return fastPower(a,b,n//2)**2*a % b
    return fastPower(a,b,n//2)**2 % b