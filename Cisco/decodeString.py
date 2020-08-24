
# 可以用stack
# input (ab(d){3}){2}
# (abddd){2}
# output abdddabddd
def decodeString(s):
    string = num = ""
    stack = []
    for char in s:
        if char == "(":
            stack.append(string)
            string = ""
        elif char == ")":
            pass
        elif char == "{":
            num = ""
        elif char == "}":
            prefix = stack.pop()
            string = prefix + int(num)* string
        elif char.isdigit():
            num += char
        elif char.isalpha():
            string += char
    return string
s = "(ab(d){3}){2}"
print(decodeString(s))

