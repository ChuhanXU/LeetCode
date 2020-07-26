class Solution:
    """
    @param s: the matrix
    @return: the last substring of s in lexicographical order
    """

    def maxSubstring(self, s):
        # Write your code here.
        cur_max = 'a'
        candiates_pos = []
        for i in range(len(s)):
            if s[i] >= cur_max:
                if s[i] > cur_max:
                    candiates_pos = []
                candiates_pos.append(i)
                cur_max = s[i]

        if len(candiates_pos) == 1:
            return s[candiates_pos[0]:]

        prepos = candiates_pos[0]

        for i in range(1, len(candiates_pos)):
            curpos = candiates_pos[i]
            #i + 1 < len(candiates_pos)表示如果存在第三个字符，candiates_pos[i + 1] - candiates_pos[i] == 1表示第二个最大字符与第三个最大字符相邻
            # 如果满足这个条件可以直接跳过第三个最大的字符，因为第二个最大字符的后一位也是最大字符，一定会大于第三最大字符开头的字串
            # 这个条件只是优化了算法
            while i + 1 < len(candiates_pos) and candiates_pos[i + 1] - candiates_pos[i] == 1:
                i += 1
            #     k 遍历的是 在最大字符后需要比较的字符的位置， 如果发现当前的字符的后一位要大于现在的字符的后一位，就更新prepos为curpos
            for k in range(1,len(s) - curpos):
                if s[curpos + k]<s[prepos + k] :
                    break

                if  s[curpos + k]>s[prepos + k] :
                    prepos = curpos
                    break;

        return s[prepos:]
    print(maxSubstring(object,"acbcab"))