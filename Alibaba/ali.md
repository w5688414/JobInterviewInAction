```
光明小学的小朋友们要举行一年一度的接力跑大赛了，但是小朋友们却遇到了一个难题：设计接力跑大赛的线路，你能帮助他们完成这项工作么？
光明小学可以抽象成一张有N个节点的图，每两点间都有一条道路相连。光明小学的每个班都有M个学生，所以你要为他们设计出一条恰好经过M条边的路径。
光明小学的小朋友们希望全盘考虑所有的因素，所以你需要把任意两点间经过M条边的最短路径的距离输出出来以供参考。

你需要设计这样一个函数：
res[][] Solve( N, M, map[][]);
注意：map必然是N * N的二维数组，且map[i][j] == map[j][i]，map[i][i] == 0，-1e8 <= map[i][j] <= 1e8。（道路全部是无向边，无自环）2 <= N <= 100, 2 <= M <= 1e6。要求时间复杂度控制在O(N^3*log(M))。

map数组表示了一张稠密图，其中任意两个不同节点i,j间都有一条边，边的长度为map[i][j]。N表示其中的节点数。
你要返回的数组也必然是一个N * N的二维数组，表示从i出发走到j，经过M条边的最短路径
你的路径中应考虑包含重复边的情况。

样例：

N = 3
M = 2
map = {
{0, 2, 3},
{2, 0, 1},
{3, 1, 0}
}


输出结果result为：
result = {
{4, 4, 3},
{4, 2, 5},
{3, 5, 2}
}

样例解释：
1->1有两种方法：1->2->1（长度为2+2=4），1->3->1（长度为3+3=6）
2->2有两种方法：2->1->2（长度为2+2=4），2->3->2（长度为1+1=2）
3->3有两种方法：3->1->3（长度为3+3=6），3->2->3（长度为1+1=2）
1->2只有一个方法：1->3->2（长度为3+1=4）
1->3只有一个方法：1->2->3（长度为2+1=3）
2->3只有一个方法：2->1->3（长度为2+3=5）
根据对称性可以得到其它部分的答案
```


print('输入范例：')
n = int(input())
m = int(input())
n_shape = input()
map = []
for i in range(n):
    line = [int(x) for x in input().split()]
    map.append(list(line))
# n, m = 3, 2
# map = [[0, 2, 3], [2, 0, 1], [3, 1, 0]]
# n, m = 4, 3
# map = [[0, 2, 4, 3], [2, 0, 5, 3], [4, 5, 0, 4], [3, 3, 4, 0]]
res = [([float('inf')]*n)for _ in range(n)]
 
 
def solve(n, m, distance):
    if m == 0:
        if res[source][n] > distance:
            res[source][n] = distance
            return
        return
    info = map[n]
    for i, j in enumerate(info):
        if j != 0:
            mypath(i, m-1, distance + j)
    return
 
 
for i in range(n):
    source = i
    solve(i, m, 0)
 
print('输出范例：')
for i in res:
    print(i)


n = int(input())
m = int(input())
n_shape = input()
map = []
for i in range(n):
    line = [int(x) for x in input().split()]
    map.append(list(line))

res = [([float('inf')]*n)for _ in range(n)]
 
 
def solve(n, m, dis):
    if m == 0:
        if res[source][n] > dis:
            res[source][n] = dis
            return
        return
    line = map[n]
    for i, j in enumerate(line):
        if j != 0:
            solve(i, m-1, dis + j)
    return
 
 
for i in range(n):
    source = i
    solve(i, m, 0)
 
for i in res:
    print(i)
