
# 样例 1:
# 	输入: list1 = null, list2 = 0->3->3->null
# 	输出: 0->3->3->null
#
#
# 样例2:
# 	输入:  list1 =  1->3->8->11->15->null, list2 = 2->null
# 	输出: 1->2->3->8->11->15->null
# 基本思想：将两条链表的节点按从小到大的顺序用一根线依次串起来，这根线就是新建一个dummy node 对应的 tail 指针，即 tail.next 不断指向两条链表中更小的一个节点，将所有节点串起来即可！
#
# 整个过程只需新建一个 dummy node，其余节点均来自两条链表，因此空间复杂度是 O(1)，时间复杂度就是遍历两条链表，因此是 O(n)，n 是两条链表长度之和。
#
# 具体做法：两个链表分别维持自己的指针 l1、l2，分别指向各自待比较的下一个节点，将两条链表的元素两两比较，谁的更小，则 tail.next 指向谁，并将较小的链表的指针指向下一个节点，而较大的链表的指针不动。如此进行下去，直到某条链表为空，最后，将可能 不空的一条链表的所有剩余节点全部串到 tail 上。
def mergeTwoList(l1,l2):
    dummy = ListNode(None)
    tail = dummy
    while l1 and l2:
        if l1.val<l2.val:
            tail.next = l1
            l1=l1.next
        else:
            tail.next = l2
            l2=l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next
