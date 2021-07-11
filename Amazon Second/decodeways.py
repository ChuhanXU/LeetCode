
# there are three end conditions
def decode(s):
    if len(s)==0:
        return 0
    ways = {}
    return dfs(s,ways),ways


def dfs(s,ways):
    if s in ways:
        return ways[s]
    if len(s)==0:
        return 1
    if s[0]=="0":
        return 0
    if len(s)==1:
        return 1
    s=s[1:]
    num = dfs(s,ways)
    prefix = s[0:2]
    if int(prefix)<=26:
        s=s[2:]
        num+=dfs(s,ways)
    ways[s]=num
    return num
s="2213"
print(decode(s))
# print(int("12"))

# 2 2 1 3
# 2 2 13
# 2 21 3


# 22 13
# 22 1 3

# 1223
# 1 2 2 3
#
# 223 23