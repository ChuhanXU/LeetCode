
# 按照size把string拆分成大小不等的片段， 然后 每两个互换位置
#     input: s = "descognail",  size = [3, 3, 2, 2]
#     expected output: "codesignal"
def concatenateSwaps(string,size):
    if len(string)==0 or len(size)==0:
        return ""

    # [0, 3, 2, 3, 1, 1]
    hash = {}
    n = len(size)
    a=0
    b=size[0]
    for i in range(n-1):
        hash[i]=string[a:b]
        a+=size[i]
        b+=size[i+1]
    hash[n-1]=string[-size[-1]:]
    value_list = list(hash.values())

    for i in range(0,n-1,2):
        value_list[i],value_list[i+1]=value_list[i+1],value_list[i]
    return "".join(value_list)


string = "descognail"
size = [3, 2, 3, 1, 1]
print(concatenateSwaps(string,size))
