
# prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]
# if we want to take 0 we must take 1 first
import collections
# time complexity O(V+E)
# graph = {0:[1,2],1:[3],2:[3],3:[]} O(E)

# degree={0:2,1:1,2:1,3:0} O(V)

# if the degree is 0 so we can put this course to queue
# queue=[3]
# pop the first element in the queue and go through the graph to check which course has 3 as their previous course
# we can find 1 and 2 have 3 as previous course , so we minus these two courses'degree
# if the degree is zero , append to queue
# queue[2,1]
# while len(queue)!=0:
# now = queue.popleft()
# we can have a course variable n if n==numCourse return True
# O(V+E)
def can(numCourses,prerequisites):
    hashCourse = {}
    hashDegree = {}
    n=0
    for i in range(numCourses):
        hashCourse[i]=[]
        hashDegree[i]=0
    for item in prerequisites:
            hashCourse[item[1]].append(item[0])
            hashDegree[item[1]] += 1
    queue = collections.deque()
    num_course = 0
    topo_order = []
    for key,value in hashDegree.items():
        if value == 0:
            queue.append(key)
    while queue:
        now_pos = queue.popleft()
        num_course += 1
        topo_order.append(now_pos)

        for key,value in hashCourse.items():
            if now_pos in value:
                value.remove(now_pos)
                hashDegree[key]-=1
                if hashDegree[key]==0:
                    queue.append(key)
    if numCourses==num_course:
        return topo_order

prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]
print(can(4,prerequisites))