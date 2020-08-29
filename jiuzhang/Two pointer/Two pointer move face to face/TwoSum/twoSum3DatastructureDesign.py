# https://www.jiuzhang.com/problem/two-sum-iii-data-structure-design/
# 设计实现一个TwoSum类，支持 add find操作
# add使用hash记录每一个元素的count
# find for循环 hash 的key set，看是否value-key在hash列表中，并检查count是否为0
# 考虑添加的时候要不要有序加入
class TwoSum:
    def __init__(self):
        self.nums = []
        self.count={}
    # 1.维护有序 直接插入法 O(n)，通过不断交换来维护数组的有序性，比较前一个数是否比这个数大
    # def add(self,number):
    #     self.nums.append(number)
    #     index = len(self.nums)-1
    #     while index>0 and self.nums[index-1]>self.nums[index]:
    #         self.num[index-1],self.num[index]=self.num[index],self.num[index-1]
    #         index-=1
    # 2. 使用hash表存
    def add(self,number):
        if number in self.count:
            self.count[number]+=1
        else:
            self.count[number]=1

    # 1.heap
    # 你以为他是sorted array，但是不是 java:priority queue,python:heapq
    # heap 其实是一个二叉树，但是存储的时候是一个数组，但是不是有序，只能知道最大最小的数是什么
    # i*2 和 i*2+1 代表左右子树，没有办法在O(1)的时间找到次小数，只能再删除最小数后调整堆得到
    #
    # 2.binary search 的插入是O(n)的

    # 3.binary Search + linked list
    # linked list 插入时O(1)的，但前提是知道应该插在哪，
    # linked list 是离线数据结构不支持 binary search O(1) index access,只能从head开头一个个找到它

    # 4.doubly linked list + hashtable
    # hashtable存的是key值 不是index

    # 5.treemap 维护的也不是一个array 红黑树 可以 log(n)的时间增删查改，用O(n)中序遍历输出array



    #         如果没有排序 find就会麻烦一点
    # hash 有序O(n)
    def find(self,value):
        for num in self.count:
            # 为了防止target为10 但是数组里只有一个5 答案却给了(5,5)的情况
            #
            if value - num in self.count and (value-num!=num or self.count[num]>1):
                return True
        return False


