# import collections
#
# DIRECTIONS = [
#     (-2, -1), (-2, 1), (-1, 2), (1, 2),
#     (2, 1), (2, -1), (1, -2), (-1, -2),
# ]
#
#
#
#
#
# def shortestPath(grid, source, destination):
#     queue = collections.deque([(source[0], source[1])])
#     distance = {(source[0], source[1]): 0}
#
#     while queue:
#         x, y = queue.popleft()
#         if (x, y) == (destination[0], destination[1]):
#             return distance[(x, y)]
#         for dx, dy in DIRECTIONS:
#             next_x, next_y = x + dx, y + dy
#             if (next_x, next_y) in distance:
#                 continue
#             if not is_valid(next_x, next_y, grid):
#                 continue
#             distance[(next_x, next_y)] = distance[(x, y)] + 1
#             queue.append((next_x, next_y))
#     return -1
#
# def is_valid(x, y, grid):
#     n, m = len(grid), len(grid[0])
#
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False
#
#     return not grid[x][y]
# matrix = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]
# visited = set()
# source = [2, 0]
# destination = [2, 2]
# print(shortestPath(matrix,source,destination))
# array = [2,3,-1,0]
# nums = list(enumerate(array))
# print(nums)

def findPosition(nums, target):
    n = len(nums)
    if n == 0:
        return -1
    start = 0
    end = n-1
    while start+1 < end:
        mid = start+(end-start)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            end = mid
        else:
            start = mid
    # 加上两个判断语句是为了防止死循环例如[1,2]的时候
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1
array = [1,2]
print(findPosition(array,2))