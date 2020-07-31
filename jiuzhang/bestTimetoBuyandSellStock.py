# 前缀和,针对这个问题不是要求和的问题，是求前缀的最小值，比如如果要求前i+1项的最小值，需要比较前i项的
# 最小值和第i+1项的值哪个更小，思想类似
# 方法一：暴力求解
# 假设第一天买入，分别求出第二，三，四，五天卖出的利润 O(n^2),然后第二天买入，第三，四，五天卖出的利润
# 方法二：前缀思想
# 假设在第i天卖出，那么应该在哪一天买入，应该在前缀最小值那一天买入

import sys
def maxProfit(prices):
 
    prefix_minimum_price = sys.maxsize
    maximum_profit = 0

    for now_price in prices:
        # 买卖完成后再更新最小值与更新完最小值再买卖结果一样
        maximum_profit = max(maximum_profit,now_price-prefix_minimum_price)
        prefix_minimum_price = min(prefix_minimum_price,now_price)
    #   prefix_minimum_price = min(prefix_minimum_price,now_price)
    #   maximum_profit = max(maximum_profit,now_price-prefix_minimum_price)
    #   倒过来写表示今天买今天卖结果是一样的，一般不符合常理
    #

    return maximum_profit
print(maxProfit([3,2,3,1,2]))