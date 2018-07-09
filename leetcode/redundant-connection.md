# problem
> In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
```
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
```
Example 2:
```
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
```
Note:
- The size of the input 2D-array will be between 3 and 1000.
- Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

# codes
```
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<int> v(2001,-1);
        for(auto edge:edges){
            int x=find(v,edge[0]);
            int y=find(v,edge[1]);
            if(x==y) return edge;
            v[x]=y;
        }
        return {};
    }
    int find(vector<int> v,int i){
        while(v[i]!=-1){
            i=v[i];
        }
        return i;
    }
};
```

# analysis
>开始表示每个结点都是一个单独的组，所谓的Union Find就是要让结点之间建立关联，比如若v[1] = 2，就表示结点1和结点2是相连的，v[2] = 3表示结点2和结点3是相连的，如果我们此时新加一条边[1, 3]的话，我们通过root[1]得到2，再通过v[2]得到3，说明结点1有另一条路径能到结点3，这样就说明环是存在的；如果没有这条路径，那么我们要将结点1和结点3关联起来，让v[1] = 3即可

# reference
[[LeetCode] Redundant Connection 冗余的连接][1]

[1]: http://www.cnblogs.com/grandyang/p/7628977.html