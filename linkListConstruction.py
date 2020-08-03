class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # 如果head是空，那tail肯定也是空
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # 如果没有tail，说明这个linked list is none,使用setHead()新建链表
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        # 因为是双向链表，所以如果要把3插入到2的前面，除了要改变3的前后指针，还要
        # 让1的后指针指向3，和2的前指针指向1，但是不确定node的前面有没有节点，如果
        # 没有的话，要将插入的节点设置为头节点
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # 插在指定位置的前一个位置
        if position == 1:
            self.setHead(nodeToInsert)
            return
        # 先找到位置对应的节点，然后调用insertBefore
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
        node = node.next

        if nodeToRemove.value == value:
            self.remove(nodeToRemove)


def remove(self, node):
    if node == self.head:
        self.head = self.head.next
    if node == self.tail:
        self.tail = self.tail.prev
    self.removeNodeBindings(node)


def removeNodeBindings(self, node):
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev
    node.prev = None
    node.next = None


def containsNodeWithValue(self, value):
    # Write your code here.
    node = self.head
    while node is not None and node.value != value:
        node = node.next
    return node is not None

