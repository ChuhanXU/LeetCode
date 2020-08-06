# 需要把 i=0 单独提出来
def query (prefix_sum,i,j):
    if i == 0:
        return prefix_sum[j]
    else:
        return prefix_sum[j]-prefix_sum[i-1]