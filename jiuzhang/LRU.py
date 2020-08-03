#使用hash列表来实现get函数，使用doubly linked list 来确定 least recently visited
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def setHeadTo(self,node):
        # 如果要插入的节点已经是head，return directly
        if self.head == node:
            return
    #     如果该链表没有一个节点，需要将Head和tail都设置为this node
        elif self.head is None:
            self.head = node
            self.tail = node
        #  if there is only one node in this linked list, set this node to head,and set node.next to tail
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        #     normaly situation that has original head and tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        # 如果就只有一个节点，将head和tail都置为空
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None






class DoublyLinkedListNode:
    def __init__ (self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
#     delete the node 4 pointers
    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None





class LRUCache:
    def __init__(self,maxSize):
        self.cache={}
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    def insertKeyValuePair(self,key,value):
        # 如果hash里没有这个key，就只能选择添加，不能用replace
        # 添加的话要分清楚这个cache有么有达到最大值，达到最大值就要移出least recently visited
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key,value)
        else:
            self.replaceKey(key,value)
        self.updateMostRecent(self.cache[key])
    #     get 完后一点要更新

    def getValueFromKey(self,key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value
    #     拿到head
    def getMostRecentKey(self):
        if self.listOfMostRecent.head is None:
            return None
        return self.listOfMostRecent.head.key
    # 删掉tail,cache 和listOfMostRecent都要删
    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def replaceKey(self,key,value):
        if key not in self.cache:
            raise Exception("The provided key isn't in the cache")
        self.cache[key].value = value



    def updateMostRecent(self,node):
        self.listOfMostRecent.setHeadTo(node)



LRU = LRUCache(3)
LRU.insertKeyValuePair(1,1)
LRU.insertKeyValuePair(2,2)
LRU.insertKeyValuePair(4,5)
LRU.insertKeyValuePair(3,3)
print(LRU.cache)