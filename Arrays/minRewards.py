def minRewards(scores):
    reward = [1 for _ in scores]
    for i in range(len(scores)):
        j = i + 1
        if scores[j] > scores[i]:
            reward[j]=reward[i]+1
        else:
            while i >= 0 and scores[j] < scores[i]:
                reward[i] = max(reward[i], reward[i+1] + 1)
                i -= 1
    return reward

print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))