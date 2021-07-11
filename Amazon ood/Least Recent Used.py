
# first i want to have a list for the question requirements to make sure i understand every functions in this question
# 1.initialize a LRU cache with specific size
# array=[]
# cache


# def get(int key):
# if key in the cache:
# return hash[key]
# while key in array
# array.remove(key)
# array.append(key)
# else: return -1


# the last element would be the most recently used
# so if we need to element we should delete the first one of array

# def put(key,value):
#  if len(cache)<size is not full
# cache[key]=value
# else len(cache)==size:
# we need to find the least recently used element from array
# cache.pop(array[0])
# array.remove(array[0])
# cache[key]=value
# array.append(key)

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru = []

    def get(self, key):
        if key in self.cache:
            if key in self.cache:
                self.lru.remove(key)
                self.lru.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
            self.lru.remove(key)

        elif len(self.cache) == self.capacity:

            self.cache.pop(self.lru[0])
            self.lru.remove(self.lru[0])

        self.cache[key] = value
        self.lru.append(key)
        return self.cache


solution = LRUCache(2)
print(solution.put(1,1))
print(solution.put(2,2))
print(solution.get(1))

def count(words):
    hash = {}
    for item in words:
        if item not in hash:
            hash[item]=1
        else:
            hash[item]+=1
    for key,value in hash.items():
        if value==1:
            return key


words=['red', 'blue', 'red', 'green', 'blue', 'blue']
print(count(words))


# class Node(self,key,val):
#     self.key = key
#     self.val = val
#     self.pre = None
#     self.next = None
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = tail
        self.tail.pre = head

    def get(self, key):
        if key in self.cache:
            self.add(cache[key])
            self.remove(cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
            self.remove(cache[key])

        elif len(self.cache) == self.capacity:

            self.cache.pop(self.head.next.key)
            self.remove(self.head.next)

        self.cache[key] = Node(key, value)
        self.add(Node(key, value))

    def add(self, node):
        p = self.tail.pre
        p.next = node
        node.next = self.tail
        node.pre = p
        self.tail.pre = node

    def remove(self, node):
        p = node.next
        p.pre = self.head
        self.head.next = p












