# 扫描线问题
def maxIncreaseKeepingSkyline(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid:
        return 0
    row = len(grid)
    col = len(grid[0])

    sum_ = 0

    for i in range(row):
        # 找到第1~n行的最大值，修改第一行第一个元素，第二个元素。。。
        max_i = max(grid[i])
        for j in range(col):
            # 找到每一列的最大元素
            max_j = max([row[j] for row in grid])
            maximum = min(max_i, max_j)#比较第一行和第一列的最大元素，最小值就是grid(1,1)的最大值
            if grid[i][j] < maximum:
                sum_ += maximum - grid[i][j]

    return sum_
matrix=[[3,0,8,4],
    [2,4,5,7],
    [9,2,6,3],
    [0,3,1,0]

]
print(maxIncreaseKeepingSkyline(matrix))

