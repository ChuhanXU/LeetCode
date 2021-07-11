
# 描述
# 哈希表容量的大小在一开始是不确定的。如果哈希表存储的元素太多（如超过容量的十分之一），我们应该将哈希表容量扩大一倍，并将所有的哈希值重新安排。假设你有如下一哈希表：
#
# size=3, capacity=4
#
# [null, 21, 14, null]
#        ↓    ↓
#        9   null
#        ↓
#       null
# 哈希函数为：
#
# int hashcode(int key, int capacity) {
#     return key % capacity;
# }
# 这里有三个数字9，14，21，其中21和9共享同一个位置因为它们有相同的哈希值1(21 % 4 = 9 % 4 = 1)。我们将它们存储在同一个链表中。
#
# 重建哈希表，将容量扩大一倍，我们将会得到：
#
# size=3, capacity=8
#
# index:   0    1    2    3     4    5    6   7
# hash : [null, 9, null, null, null, 21, 14, null]
# 给定一个哈希表，返回重哈希后的哈希表。
# 重建一个doublesize的hashtable, 然后取出原哈希table中的所有空元素
# 将该元素的值传给addnode函数，经过计算得到该值的hashcode的index，如果该index被占用
# 则在该位置上生成一个链表，将元素添加至链表的尾部

# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def rehashing(self,hashTable):
    HASH_SIZE  = 2*len(hashTable)
    doubleHashtable = [None for i in range(HASH_SIZE)]
    for item in hashTable:
        p=item
        while p!=None:
            self.addNode(doubleHashtable,p.val)
            p = p.next
    return doubleHashtable


def addNode(self,doubleHashtable,value):
    #     计算hashcode
    index = value % len(doubleHashtable)
#     如果该index为空,直接放入一个以此value开头的list
    if doubleHashtable[index]==None:
        doubleHashtable[index]=ListNode(value)
    else:
        self.addlistNode(doubleHashtable[index],value)


def addListNode(self,node,value):
    if node.next == None:
        node.next = ListNode(value)
    else:
        self.addListNode(node.next,value)

