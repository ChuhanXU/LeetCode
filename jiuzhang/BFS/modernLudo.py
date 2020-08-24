import collections


def modernLudo (length,connections):
    # 建图
    transport = [set() for _ in range(length+1)]
    for u,v in connections:
        transport[u].add(v)

    queue = collections.deque()
    # dist记录的是到达不同位置需要多少次撒子
    dist = {}

    queue.append(1)
    dist[1]=0

    while queue:
        now = queue.popleft()
        # 处理当两个传送门连在一起的情况
        # dist[next_pos]<= dist[now]有些点传送门已经走过了就被跳过了,比如说[7,9][8,14]
        # 当我走到3的时候（3+6=9），9已经被放入到了队列一次，但这时候并不知道9也有传送门，所以要多加一个限制条件，如果之前的次数比现在小可以continue，否则还是要把这个9放入队列

        for next_pos in transport[now]:
            if next_pos in dist and dist[next_pos]<= dist[now]:
                continue
            queue.append(next_pos)
            # 因为是连着的传送门所以dist[]应该相同
            dist[next_pos] = dist[now]

        for i in range(1,7):
            next_pos = now + i

            if next_pos > length:
                break
            # 对于不在dist里的位置，说明我们可以通过掷色子到达这个位置，dist[now]表示到达这个位置
            # 掷色子的次数
            if next_pos not in dist:
                queue.append((next_pos))
                dist[next_pos] = dist[now]+1
#             还需要把传送门out的位置也放入到队列中去
                for out in transport[next_pos]:
                    if out not in dist:
                        queue.append(out)
                         # 因为是传送门的缘故所以不需要+1
                        dist[out]=dist[next_pos]
    return dist[length]
# connections= [[2, 8],[6, 9]]
# print(modernLudo2(15,connections))
# bfs的一个小技巧

# while queue:
#     now
#     所有对当前点的操作再出队的时候进行操作，比如加入记录什么什么的
#     for 所有next的点（再这里只对now.next进行操作，而不是找now.next.next）
#     在后面只要找到下一个点就好

# 1.对于每个点的状态改变，加入答案，自出队时进行操作
# 2.所有找next的操作放在对于当前点状态改变后
# 第二种做法，通过建图来做，传动门对应边长为0，扔撒子对应为1
# 直接把边变成我需要的边，有点类似迪杰斯特拉做法
def modernLudo2(length,connections):
    edge = [{}for _ in range(length + 1)]
    # i 1-15
    for i in range(1,length):
        for j in range(1,7):
            edge[i][i+j] = 1
    # 传送门的边
    for u,v in connections:
        edge[u][v] = 0

    queue = collections.deque()
    dist={}

    queue.append(1)
    dist[1]= 0

    while queue:
        now = queue.popleft()
        for next_pos in edge[now]:
            if next_pos > length:
                break
            if next_pos in dist and dist[next_pos]<=dist[now]+edge[now][next_pos]:
                continue
            #     continue的话说明原方案更好，不然的话需要将next_pos加入队列
            queue.append(next_pos)
            dist[next_pos]=dist[now] + edge[now][next_pos]
    return dist[length]
connections= [[2, 8],[6, 9]]
print(modernLudo2(15,connections))