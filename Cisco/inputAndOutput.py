# your_input=raw_input('please input your name:')
# inputArray = list(map(int,your_input.split()))
# inputString = your_input.replace(" ","")
# print('your name is :', inputString)
# print('your name is :', inputArray)
# print(type(your_input))
# input = 6
# input = 2 -8 3 -2 4 -10

inputOfNum = input()
inputOfList = input()
n=int(inputOfNum)
array = list(map(int,inputOfList.split()))

def continuousSubarray(n,array):
    for i in range(1,n):
        if array[i-1]>0:
            array[i]+=array[i-1]

    return max(array)

print(continuousSubarray(n,array))
