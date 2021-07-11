
# Input:
#   push(1)
#   pop()
#   push(2)
#   push(3)
#   min()
#   push(1)
#   min()
# Output:
#   1
#   2
#   1
# 需要构建一个辅助栈维护最小值，如果加入的值小于栈顶元素则加入min_stack，否则的话再加入一次当前的栈顶元素
class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def push(self,number):
        self.stack.append(number)
        if not self.min_stack or number <= self.min_stack[-1]:
            self.min_stack.append(number)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()


    def min(self):
        return self.min_stack[-1]
