
# input
# cutOffRank = 4
# num = 5
# scores=[2,2,3,4,5]

# output 5
def cutoffrank(cutoffrank,num,scores):
    scores = sorted(scores,reverse=True)
    while cutoffrank<num:
        if scores[cutoffrank-1]==scores[cutoffrank]:
            cutoffrank+=1
        else:
            return cutoffrank
    return cutoffrank
# scores=[2,2,3,4,5]
scores=[100,50,50,25]
print  (cutoffrank(3,4,scores))

