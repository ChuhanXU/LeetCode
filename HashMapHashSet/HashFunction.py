def hashCode(key,HASH_SIZE):
    ans = 0
    for x in key:
        ans = (ans*33+ord(x))%HASH_SIZE
    return ans
print(hashCode('abc',100))