
# input
# num 5
# stockPriceDelta=[4,2,12,11,-5]
# windowSize = 2

def windowMinimums(num,stockPriceDelta,windowSize):
    if len(stockPriceDelta)==0 or windowSize==0:
        return []
    result = []
    left=0
    right=left+windowSize-1
    while right<num:
        current=sorted(stockPriceDelta[left:right+1])
        result.append(current[0])
        left+=1
        right+=1
    return result
stockPriceDelta=[4,2,12,11,-5]
print(windowMinimums(5,stockPriceDelta,2))
