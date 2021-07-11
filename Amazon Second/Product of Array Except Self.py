class Solution:
    def productExceptSelf(self,nums):
        preProduct = 1
        postProduct = 1
        result = [1]*len(nums)

        for i in range(len(nums)):
            result[i]=result[i]*preProduct
            preProduct=preProduct*nums[i]
        for i in range(len(nums)-1,-1,-1):
            result[i]=result[i]*postProduct
            postProduct=postProduct*nums[i]
        return result