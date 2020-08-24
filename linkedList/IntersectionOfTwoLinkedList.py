class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
    # 1. how can you make sure they will always meet at the intersection
    # we can keep track of the total distance traveled by those two pointers,
    # right so if you look at pointer number 1 see the total distance that pointer 1
    # has traveled is A plus B plus C the total summary of three segments,if we look at B
    # it will be c first B and A right, as based on our elementary school, math you know it
    # is called what associative rule right.so we can guarantee they will always meet on the
    # intersection

    # 2.如何清楚有效的表达自己的解题观点/思路
    # 凡是排好序的八九不离十要用二分法
    # since the entire array is a 2D array and all the elements are sorted, so what we need to do is first of all we are going to do what
    # perform binary search vertically
    # determine the rough range of where the target is located like every row
    # perform another binary search horizontally