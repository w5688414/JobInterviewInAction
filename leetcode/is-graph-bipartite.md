# problem
>Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
```
Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
```
```
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
```
Note:

- graph will have length in range [1, 100].
- graph[i] will contain integers in range [0, graph.length - 1].
- graph[i] will not contain i or duplicate values.
- The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

# codes
```
class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        vector<int> colors(graph.size());
        for(int i=0;i<graph.size();i++){
            if(colors[i]==0&&!isValid(graph,i,1,colors)){
                return false;
            }
        }
        return true;
    }
    bool isValid(vector<vector<int>>& graph,int cur,int color,vector<int>& colors){
        if(colors[cur]!=0) return colors[cur]==color;
        colors[cur]=color;
        for(int i:graph[cur]){
            if(!isValid(graph,i,-1*color,colors)){
                return false;
            }
        }
        return true;
    }
};
```

# analysis
>们采用一种很机智的染色法，大体上的思路是要将相连的两个顶点染成不同的颜色，一旦在染的过程中发现有两连的两个顶点已经被染成相同的颜色，说明不是二分图。
这个染色法很巧妙，我也做不出来。

# reference
[[LeetCode] Is Graph Bipartite? 是二分图么？][1]


[1]: https://www.cnblogs.com/grandyang/p/8519566.html
