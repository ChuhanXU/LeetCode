# 双指针的计数问题
# abacba right = 0 右指针一直移动到 unique_char_number >= k,right = 3
# ans += n-right=6-3=3,得到的三个子串分别为[[0,3],[0,5],[0,6]]
def kDistinctCharacters(s,k):
    n = len(s)
    left = 0
    counter = {}
    ans = 0
    unique_char_number = 0
    # 右指针为主指针
    for right in range(n):
        # 将char放入hashtable并计数
        counter[s[right]]=counter.get(s[right],0)+1

        # 如果这个数是第一次放入，这单独的字母K + 1
        if counter[s[right]] == 1:
            unique_char_number+=1
        # 进入while之前说明 unique_char_number 已经 >= k
        # 这个的处理条件是放在循环里面的，不然会漏解
        while unique_char_number >= k:
            ans += n-right
            # 需要减少对应的字母在hash中的数量
            counter[s[left]] -= 1

            if counter[s[left]] == 0:
                unique_char_number -= 1
            left += 1
    return ans
print(kDistinctCharacters("abcabcabcabc",3))


