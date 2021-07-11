# [1,2,3]
# def permutation(nums):
#     if len(nums)==0:
#         return []
#     visited = []
#     current=[]
#     result=[]
#     dfs(nums,current,visited,result)
#     return result
#
# def dfs(nums,current,visited,result):
#     if len(current)==len(nums):
#         result.append(current[:])
#         return
#     for i in range(len(nums)):
#         if nums[i] not in visited:
#             current.append(nums[i])
#             visited.append(nums[i])
#             dfs(nums,current,visited,result)
#             current.remove(nums[i])
#             visited.remove(nums[i])
# nums=[1,2,3]
# print(permutation(nums))
# [1,2,3,4] combination 为 5 的所有组合
# def combination(nums,target):
#     if len(nums)==0:
#         return[]
#     index=0
#     current=[]
#     result=[]
#     dfs(nums,index,current,result,target)
#     return result
# def dfs(nums,index,current,result,target):
#     if target==0:
#         result.append(current[:])
#         return
#     for i in range(index,len(nums)):
#         current.append(nums[i])
#         dfs(nums,i+1,current,result,target-nums[i])
#         current.remove(nums[i])
#
# nums=[1,2,3,4]
#
# print(combination(nums,5))

# bfs the shortest path from (0,0)(m-1,n-1)
# import collections
#
#
# def shorestPath(matrix):
#     m=len(matrix)
#     n=len(matrix[0])
#     directions=[(1,0),(-1,0),(0,1),(0,-1)]
#     queue=collections.deque()
#     queue.append((0,0))
#     visited=set()
#     visited.add((0,0))
#     dist={(0,0):0}
#     while queue:
#         x,y=queue.popleft()
#         for del_x,del_y in directions:
#             next_x=x+del_x
#             next_y=y+del_y
#             if valid(matrix,visited,next_x,next_y,m,n):
#                 queue.append((next_x,next_y))
#                 visited.add((next_x,next_y))
#                 dist[(next_x,next_y)]=dist[(x,y)]+1
#     if (m-1,n-1) in dist:
#         return dist[(m-1,n-1)]
#     else:
#         return -1
#
# def valid(matrix,visited,x,y,n,m):
#     if x<0 or y<0 or x>n-1 or y>m-1:
#         return False
#     if (x,y) in visited:
#         return False
#     if matrix[x][y]==1:
#         return False
#     return True
#
# matrix = [
#     [0, 1, 0],
#     [0, 0, 1],
#     [0, 0, 0]
# ]
# print(shorestPath(matrix))
#course schedule
# import collections
#
#
# def schedule(pre,numCourses):
#     if  numCourses==0:
#         return[]
#     coursePre={}
#     indegree ={}
#     order=[]
#     for i in range(numCourses):
#         coursePre[i]=[]
#         indegree[i]=0
#
#     for item in pre:
#         coursePre[item[0]].append(item[1])
#         indegree[item[0]]+=1
#     queue = collections.deque()
#
#     for key,value in indegree.items():
#         if value==0:
#             queue.append(key)
#     while queue:
#         currentCourse = queue.popleft()
#         order.append(currentCourse)
#         for key,value in coursePre.items():
#             if currentCourse in value:
#                 indegree[key]-=1
#                 if indegree[key]==0:
#                     queue.append(key)
#     if len(order)==numCourses:
#         return order
#     else:
#         return -1
# prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]
# print(schedule(prerequisites,4))

# decode tree
import collections

def __inif__TreeNode(self,val):
    self.val=val
    self.right = None
    self.left=None


def toarray(root):
    if not root:
        return None
    queue = collections.deque()
    queue.append(root)
    array=[]

    while queue:
        node = queue.popleft()
        if node:
            array.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        else:
            array.append("#")
    return ",".join(array)

def totree(self,array):
    if len(array)==0:
        return None
    array= array.split(',')
    index = 1
    queue = collections.deque()
    queue.append(self.TreeNode(int(array[0])))

    while queue:
        node = queue.popleft()
        if array[index]!="#":
            node.left = self.TreeNode(int(array[index]))
        index+=1

        if array[index]!="#":
            node.right=self.TreeNode(int(array[index]))
        index+=1
    return node



