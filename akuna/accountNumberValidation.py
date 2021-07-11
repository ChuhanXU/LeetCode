
# 给出的account可能不是8位的，而且account里面的字符可能不是[0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,A,B,C,D,E,F]中的，比如"13A38X"这种，虽然"X"不合法，parseInt("13A38X", 16)依然返回了一个十进制数字。。。
# 坑2：最后所有数字加起来可能小于15，于是.toString(16)将数字和转化成了一个只有一位的16进制数字，因此和前两位对比之前要在前面加一个"0"。。
# input BADF00D5  INVALID
# input 1CC0FfEE  VALID
def validation(account):
    if len(account)!=8:
        return "INVALID"
    list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","A","B","C","D","E","F"]
    for char in account:
        if char not in list:
            return "INVALID"
    #把 16 进制转化为 10 进制
    decimal = str(int(account[2:8],16))

    num = 0
    for i in range(len(decimal)):
        num+=int(decimal[i])
    if num<16:
        hexnum = "0"+hex(num)[2:]
    else:
        hexnum = hex(num)[2:]
    if hexnum.lower() == account[0:2].lower():

        return "VAlID"
    return "INVALID"
print(validation('1CC0FfqE'))
