
# 有一个test case 没过
import collections
def maxSlidingWindow(num_computer, hard_disk_space, segment_length):
    if segment_length > len(hard_disk_space):
        return []
    if not hard_disk_space:
        return []
    start=0
    end=start+segment_length
    result=[]
    while start<=num_computer-segment_length:
        window = hard_disk_space[start:end]
        minispace = min(window)
        result.append(minispace)
        start+=1
        end=start+segment_length
    print(result)
    return max(result)


# def maxSlidingWindow(num_computer, hard_disk_space, segment_length):
#     if segment_length > len(hard_disk_space):
#         return []
#     if not hard_disk_space:
#         return []
#
#     ret = []
#     q = collections.deque()
#
#     for i in range(len(hard_disk_space)):
#         # remove everything from the back that is >= the current num
#         while q and q[-1][0] >= hard_disk_space[i]:
#             q.pop()
#         # add the new num to the back
#         q.append((hard_disk_space[i], i))
#         # remove everything from the front if it's not in the window
#         while q[0][1] <= i - segment_length:
#             q.popleft()
#         # start adding results to output array once we have our first size k window
#         if i >= segment_length - 1:
#             ret.append(q[0][0])
#
#     return max(ret)

# 8,2 = 2
# 2,4 = 2
# 4,5 = 4
# 5,6 = 5
# 6,4 = 4
# 2 2 4 5 4 max = 5

# 824 2
# 245 2
# 456 4
# 564 4
#

print(maxSlidingWindow(8 [10,20,30,40,25,81,98,45], 8))