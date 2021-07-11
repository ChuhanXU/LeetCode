# 给一个不包含0和1的数字字符串，每个数字代表一个字母，请返回其所有可能的字母组合。
#
# 下图的手机按键图，就表示了每个数字可以代表的字母。
#
# 1
# 2
# ABC
# 3
# DEF
# 4
# GHI
# 5
# JKL
# 6
# MNO
# 7
# PQRS
# 8
# TUV
# 9
# WXYZ
# #
def phoneNumber(digit):
    phone={2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PQRS',8:'TUV',9:'WXYZ'}
    result = []
    dfs(phone,0,[],result,digit)
    return result

def dfs(phone,index,current,result,digit):
    if len(digit)==len(current):
        result.append(''.join(current))
        return

    for c in phone[int(digit[index])]:
        current.append(c)
        dfs(phone,index+1,current,result,digit)
        current.pop()
print(phoneNumber("25"))
