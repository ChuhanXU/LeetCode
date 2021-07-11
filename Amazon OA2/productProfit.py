# 绿蓝红格的
# input
# numSuppliers = 2
# inventory =[3,5]
# order = 6

# output = 19
# there are two suppliers, one with inventory 3 and the other with inventory 5,and 6 items were ordered
# 5(2rd item)+4(2rd item)+3(2rd item)+3(1st item)+2(2rd item)+2(1st item)
# maximum profit = 19
# 6+5+5+4+4+3
# [2,6]
# 4
# offset = 6-4 =2
# [1,0,0,0,1]

def highestProfit(numSuppliers, inventory, order):  # O(2m+3n) -> O(m+n)
    cur_max = max(inventory)  # O(m)
    cur_inv = [0] * (order + 1)  # O(n)
    offset = cur_max - order
    for inv in inventory:  # O(m)
        if inv < offset:
            continue
        cur_inv[inv - offset] += 1
    i, ans = order, 0
    for _ in range(order):  # O(n), 总共 O(n+n)
        while i > 0 and cur_inv[i] == 0:  # O(1)
            i -= 1
        ans += i + offset
        cur_inv[i] -= 1
        cur_inv[i - 1] += 1
    return ans
# numSuppliers = 2
# inventory =[3,5]
# order = 6
print(highestProfit(2,[2,3],6))
# def maximum(numSuppliers,inventory,order):
#     inventory = sorted(inventory,reversed=True)
#     for i in range(numSuppliers):
#         if numSuppliers[i]>numSuppliers[i-1]:
#             profit = numSuppliers[i]-numSuppliers[i-1]