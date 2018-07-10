# problem
>In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.
```
Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.
```
Note:

- graph will have length at most 10000.
- The number of edges in the graph will not exceed 32000.
- Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].

# codes
```
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n=graph.size();
        vector<int> colors(n,0);
        vector<int> res;
        for(int i=0;i<n;i++){  //dfs每个结点判断是否有环
            if(solve(graph,colors,i)){ //从i出发有环则返回false
                res.push_back(i);
            }
        }
        return res;
    }
    bool solve(vector<vector<int>>& graph,vector<int>& colors,int node){
        if(colors[node]>0){
            return colors[node]==2; //如果染色是安全状态2就返回true
        }
        colors[node]=1; //初始染1号色，相当于标记这次dfs过程中访问过它，但它的状态不确定是否安全
        for(int i:graph[node]){ //如果它的邻接点或者他的邻接点的邻接点dfs时又访问了i结点那么就说明成环了。
            if(colors[i]==2) continue;
            if(colors[i]==1||!solve(graph,colors,i)){
                return false;
            }
        }
        colors[node]=2;
        return true;
    }
};
```

# analysis
>用到了后序遍历，还有数组序列化，并且建立序列化跟其出现次数的映射，这样如果我们得到某个结点的序列化字符串，而该字符串正好出现的次数为1，说明之前已经有一个重复树了，我们将当前结点存入结果res，这样保证了多个重复树只会存入一个结点.

# reference
[802. Find Eventual Safe States][1]
[leetcode802——Find Eventual Safe States][2]

[1]: https://leetcode.com/problems/find-eventual-safe-states/solution/
[2]: https://blog.csdn.net/tzyshiwolaogongya/article/details/79653786