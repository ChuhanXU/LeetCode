# 1.sort this array by heap
# [3,4,1,2,6] => k=3
# [6,4,3]
# is using the sort function in python and got a reverse sorted array [6,4,3,2,1]
# I will use min heap to maintain the order
#       3
#     4   1
#   2  6
#       3
#    4
# child index is i,we calculate its father index is (i-1)/2

#       0
#     1   2
#   3 4  5 6
# if we have father node , left node will be 2i+1,right node will be 2i+2
# but if we have a child node, the parent node will be (i-1)/2
# then I will use evey element to compare to its father node
# if childnode > fathernode break  O(logn)
# if < swap them to maintain the order of my heap
# heap
# class solution:
#     def siftup(self,A,child):
#         while child!=0:
#             father = (child-1)//2
#             if A[child]>=A[father]:
#                 break
#             A[child],A[father]=A[father],A[child]
#             # check if the previous element is still in order
#             child=father
#     def heapify(self,A):
#         for i in range(len(A)):
#             self.siftup(A,i)
#         return A
# solution = solution()
# nums=[3,4,1,2,6]
# print(solution.heapify(nums))
# two pointer
class solution():
    def ktop(self,A,k):
        if len(A)==0:
            return[]
        nums = self.helper(A,0,len(A)-1)

        return nums[len(A)-k]
    def helper(self,A,start,end):
        if start>end:
            return
        left =start
        right = end
        pivot = A[(start+end)//2]
        #wht <= because I want to make sure when i jump out from the while loop ,left and right are not in the same position
#             locate the swap location
        while left<=right and A[left] < pivot:#why < because for special situation [1,1,1,1]
            left+=1
        while left <= right and A[right] > pivot:
            right -=1
        if left <= right:
            A[left],A[right]=A[right],A[left]
            left+=1
            right-=1
        self.helper(A,start,right)
        self.helper(A,left,end)
        return A
solution = solution()
nums=[3,4,1,2,6]
print(solution.ktop(nums,2))
# [1,4,3,2,6]




