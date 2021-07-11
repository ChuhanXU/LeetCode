def finsAnagram(strs):
    if len(strs) == 0:
        return []
    visited = set()
    hash = {}
    for i in range(len(strs)):
        for j in range(len(strs)):
            if strs[j] in visited:
                continue
            #                 aet==aet
            if sorted(strs[i]) == sorted(strs[j]):
                if tuple(sorted(strs[i])) not in list(hash.keys()):
                    hash[tuple(sorted(strs[i]))] = [strs[j]]
                else:
                    hash[tuple(sorted(strs[i]))].append(strs[j])
                visited.add(strs[j])
    return list(hash.values())

# NKlog(K)
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(finsAnagram(strs))
# print(str(sorted(strs[1])))
