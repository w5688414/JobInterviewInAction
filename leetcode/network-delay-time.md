# problem
>There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
1. N will be in the range [1, 100].
2. K will be in the range [1, N].
3. The length of times will be in the range [1, 6000].
4. All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

# codes
```
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        int res=0;
        vector<vector<int>> edges(101,vector<int>(101,-1));
        queue<int> q{{K}};
        vector<int> dist(N+1,INT_MAX);
        dist[K]=0;
        for(auto e:times){
            edges[e[0]][e[1]]=e[2];
        }
        while(!q.empty()){
            unordered_set<int> visited;
            for(int i=q.size();i>0;i--){
                int u=q.front(); q.pop();
                for(int v=1;v<=100;v++){
                    if(edges[u][v]!=-1&&dist[u]+edges[u][v]<dist[v]){
                        if(!visited.count(v)){
                            visited.insert(v);
                            q.push(v);
                        }
                        dist[v]=dist[u]+edges[u][v];
                    }
                }
            }
        }
        for(int i=1;i<=N;i++){
            res=max(res,dist[i]);
        }
        return res==INT_MAX ? -1:res;
    }
};
```

# analysis
>当有对边 (u, v) 是结点u到结点v，如果 dist(v) > dist(u) + w(u, v)，那么 dist(v) 就可以被更新，这是所有这些的算法的核心操作。Dijkstra算法是以起点为中心，向外层层扩展，直到扩展到终点为止。
- 为了防止重复比较，我们需要使用visited数组来记录已访问过的结点，最后我们在所有的最小路径中选最大的返回，注意，如果结果res为INT_MAX，说明有些结点是无法到达的，返回-1。
- 普通的实现方法的时间复杂度为O(V2)，基于优先队列的实现方法的时间复杂度为O(E + VlogV)，其中V和E分别为结点和边的个数.
# reference
[[LeetCode] Network Delay Time 网络延迟时间][1]

[1]: http://www.cnblogs.com/grandyang/p/8278115.html