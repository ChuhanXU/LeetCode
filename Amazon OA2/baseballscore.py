from pip._vendor.progress.counter import Stack


def baseball(blocks):
    if not blocks:
        return 0
    result =0
    stack = []
    for item in blocks:
        if item=="X" and len(stack)!=0:
            num = stack.peek()*2
            result+=num
            stack.append(num)
        elif item=='+' and len(stack)!=0:
            temp = stack.pop()
            num=temp
            if len(stack)!=0:
                num+=temp
            stack.append(temp)
            result+=num
            stack.append(num)
        elif item =='Z' and len(stack)!=0:
            num = stack.pop()
            result-=num
        else:
            num = int(item)
            result+=num
            stack.append(num)
    return result
blocks=['10','20','Z','30','+']
print(baseball(blocks))
