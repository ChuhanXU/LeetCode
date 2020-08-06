# 使用一个hashtable，存放字母的最后出现位置，如果遍历过程中发现同样的字母，这选取当前startIdx和hash[char]+1的较大值重新作为startIdx
def longestSubstringWithoutDuplication(string):
	lastSeen = {}
	longest = [0,1]
	startIdx = 0
	for i,char in enumerate(string):
		if char in lastSeen:
            # 这个地方要做一次比较是为了防止遍历到第二个c的时候回到l，而是应该保持当前的较大值startIdx 3 m
			startIdx = max(startIdx,lastSeen[char]+1)
		if longest[1]-longest[0] < i+1-startIdx:
			longest = [startIdx,i+1]
		lastSeen[char] = i
	return string[longest[0]:longest[1]]



print(longestSubstringWithoutDuplication("clementisacap"))