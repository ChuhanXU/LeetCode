def competitiveGame(n,k,scores):
    scores = sorted(scores)
    count = 1
    level = 1
    pre = scores[0]
    for i in range(1,n,1):
        if scores[i]==0:
            break

        if scores[i]!=pre:
            pre = scores[i]
            level = i+1

        if level <= k:
            count+=1

        else:
            break
    return count

scores = [20,20,30,100]
print(competitiveGame(4,1,scores))
