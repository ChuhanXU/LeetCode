
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to,
# or null if it does not point to any node.
# input head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# output head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None
        dict={}
        prev=None
        node=head#只是一个reference索引
        while node:
            if node not in dict:
                dict[node]=Node(node.val,node.next,node.random)
            if prev:
              # 让上一个节点指向新复制的节点
                prev.next = dict[node]
            else:
                head = dict[node]#if there is no prev,then we are at the head.store it to the return later
            if node.random:
                if node.random not in dict:
                    dict[node.random]=node(node.random.val,node.random.next,node.random.random)
                dict[node].random=dict[node.random]
            prev,node = dict[node],node.next
        return head

n1 = Node(7,n2,None)
n5 = Node(1,None,n1)
n4 = Node(10,n5,n3)
n3 = Node(11, n4, n5)
n2 = Node(13,n3,n1)











