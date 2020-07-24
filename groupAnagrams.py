# 时间复杂度 nmlogm 空间复杂度 mn n是列表中单词的数量，m是列表中最长单词字母的数量the number of the longest words
def groupAnagrams(words):
	anagrams={}
	for word in words:
        # 给word按字母顺序排序 reorder word in Alphabetical order
        # hashtable中的value是未按字母排序的anagram
		sortedWord = "".join(sorted(word))
        # 如果 hash table 里有这个word就将此word(未按字母排序)放入对应的hashtable中去，{"oy":["yo","oy"],"act":["act","tac","cat"]}
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
            # 如果没有，在hash table对应位置创建dic,这个value一定是数组形式，不然不能append
			anagrams[sortedWord]=[word]
	return list(anagrams.values())
print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))