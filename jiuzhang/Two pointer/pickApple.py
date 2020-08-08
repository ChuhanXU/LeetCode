# 摘苹果问题：双指针加遍历隔板
def pickApples(num,x,y):
    # 得出left_A[i],left_[B],right_A[i],right_B[i]
    # left_A[i]表示 A 在前i棵树上可以摘到的苹果,right_A[i]
    # 枚举隔板:i
    # ans = max(ans,max(left_A[i]+right_B[i+1],left_B[i]+right_A[i+1]))
    n = len(num)
    if x + y > n:
        return -1
    # get_left 这个方法是为了得到在前半部分区间每个位置所能摘到的最多的苹果树数量
    left_A = get_left(num,x)
    left_B = get_left(num, y)
    print(left_A,left_B)
    # 如何得到后半部分的每个位置所能摘到的苹果树的最多数量
    # 先将数组整个倒过来，重复get_left的操作，然后再倒过来
    temp_num = num[::-1]

    right_A = get_left(temp_num,x)
    right_B = get_left(temp_num,y)
    print(right_A, right_B)

    right_A = right_A[::-1]
    right_B = right_B[::-1]

    ans = -1
    # 遍历隔板的位置，隔板的范围应该是多少
#     隔板应该把数组分割为[0,i][i+1,n-1],所以i+1的最大值应该为n-1，所以i的最大值为n-2
    for i in range(n-1):
        temp_maximum = -1
        # 先要将隔板遍历到大于A人可以摘到苹果树的数量的位置，比如 A 要求的苹果树数量为3，所以再index为0，1
        # 的位置的时候最大数量就是-1
        # A在前,B在后
        if left_A[i]!=-1 and right_B[i+1]!=-1:
            temp_maximum = max(temp_maximum,left_A[i]+right_B[i+1])
        # B在前,A在后
        if left_B[i] != -1 and right_A[i + 1] != -1:
            temp_maximum = max(temp_maximum, left_B[i] + right_A[i + 1])
        ans = max(ans,temp_maximum)
    return ans
# 双指针找连续的值和最大区间
def get_left(num,k):
    n = len(num)
    left = 0
    right = k-1
    now_sum = 0
    # for 循环记录了前K个的和
    for i in range(k):
        now_sum += num[i]
    left_arr = [-1] * n
    now_maximum = now_sum
    left_arr[right] = now_sum
    while right < n-1:
        right += 1
        now_sum += num[right]
        now_sum -= num[left]
        left += 1
        now_maximum = max(now_maximum,now_sum)
        left_arr[right] = now_maximum
    return left_arr

print(pickApples([6, 1, 4, 6, 3, 2, 7, 4],3,2))






