
# 由于用了路径压缩，将并查集的时间复杂度从O(n)压缩到了O(1),因此总的时间复杂度为O(k*1),k为操作次数
# 并查集适用于当你需要永久修改地图中某一元素时,如果使用BFS,你需要每一次修改后都在运行一遍BFS,并查集可以实现动态的BFS
# 并查集是指用集合里的一个元素来当这个集合的代表元
# 如果两个元素所在的集合的代表元相同,那么我们就能知道这两个元素在一个集合中
# 如果我们想合并两个集合，如果我们想合并两个集合，只需要把其中一个集合的代表元改为第二个集合的代表元
# in this question, everytime we changed one ocean to island, we need to make the number of island plus 1
# then check if there is another islands around this island using BFS
# if yes, we need to check if these two islands are in the same union find
# if they are not in the same set, that indicate that they are connected, what we need to do is to merge them to
# one union find and make the total number of islands minus 1
# if they are in same union find,do nothing
# we finished merge when we make both of them in one union find,要让i所在集合的代表元改为j所在集合的代表元
# 注意，数据中有可能多次将一个位置变成岛屿，第一次以后的操作都是无效操作，跳过
# 路径压缩
# 注意2：x->x1->x2->x3->x4->x5->x6->........->代表元T
# 我们在第一次寻找x的代表元的回溯的时候
#
# 顺便把这条路径的所有xi的父亲改为了代表元T
#
# 这样我们以后再次访问x....x6....T这条链上的内容时候就可以很快的得到答案