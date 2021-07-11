
# 1 0 2 2 1 3
#1 - A
#2 - B
#index
# 0
# 1

# 1 2
# A B
# 12
# L

#corner case
# >26
# 0
# 10 2
# 1 0 2
#
# 1 0 2 2 1 3
# 1 0 1 2

# empty

class Solution(object):
    def numDecodings(self, s):
        memo = [None]*(len(s)+1)
        index=0
        self.dfs(s,memo,index)
        return memo[index]
    def dfs(self,s,memo,index):
        if index==len(s):
            return 1
        if s[index]=="0":
            return 0
        if memo[index]!=None:
            return memo[index]
        way1=self.dfs(s,memo,index+1)
        way2=0
        if index<=(len(s)-2) and int(s[index:index+2])<=26:
            way2=self.dfs(s,memo,index+2)
        memo[index]=way1+way2
        return memo[index]
# class Solution(object):

    # def numDecodings(self, s):
    #     memo = [None] * (len(s) + 1)
    #     print(memo)
    #     return self.helper(s, 0, memo)
    #
    # def helper(self, s, index, memo):
    #     # if the substring is 0
    #     if index == len(s):
    #         return 1;
    #     # if the first character of substring is 0
    #     if s[index] == '0':
    #         return 0
    #     # to get the calculated ways of substring directly
    #     if memo[index] != None:
    #         return memo[index]
    #
    #     way1 = self.helper(s, index + 1, memo)
    #     way2 = 0
    #     # there are two options take the first character of the first two characters, if the two number < 26 indicates way2 is not equal to 0
    #     if index < len(s) - 1 and int(s[index:index + 2]) <= 26:
    #         way2 = self.helper(s, index + 2, memo)
    #     memo[index] = way1 + way2
    #     return memo[index]
s='102213'


solution = Solution()
print(solution.numDecodings(s))


