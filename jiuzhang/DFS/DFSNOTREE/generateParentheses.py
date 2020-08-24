
# 生成括号
# 输入 3
# 当前用了的右括号多余左括号数量，停止
# 如果括号放完了也没出现什么问题，就添加这种答案
# 在dfs函数中第一步写出口,通常dfs函数的参数中会传入最后想return的答案

def generateParentheses(n):
    if n == 0:
        return []
    result = []
    dfs(n,n,'',result)
    return result
# remaining number of parentheses
def dfs(left_count,right_count,path,result):
    if left_count == 0 and right_count == 0:
        result.append(path)
    #     如果剩余的右括号小于剩余的左括号，就不行了
    if right_count < left_count:
        return

    if left_count>0:
        dfs(left_count-1,right_count,path+'(',result)

    if right_count > 0:
        dfs(left_count,right_count-1,path+')',result)

print(generateParentheses(3))
