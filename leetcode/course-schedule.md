# problem
>There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Example 1:
```
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```
Example 2:
```
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```
Note:
- The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
- You may assume that there are no duplicate edges in the input prerequisites.

# codes
```
class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<int>> graph(numCourses,vector<int>(0));
        vector<int> inDegree(numCourses,0);
        for(auto k:prerequisites){
            graph[k.second].push_back(k.first);
            inDegree[k.first]++;
        }
        queue<int> que;
        for(int i=0;i<numCourses;i++){
            if(inDegree[i]==0){
                que.push(i);
            }
        }
        while(!que.empty()){
            int u=que.front();
            que.pop();
            for(auto v:graph[u]){
                inDegree[v]--;
                if(inDegree[v]==0){
                    que.push(v);
                }
            }
        }
        for(int i=0;i<numCourses;i++){
            if(inDegree[i]!=0){
                return false;
            }
        }
        return true;
    }
};
```

# analysis
>这是我刷的第一道图论的题目，我没有做出来，但是我觉得思路不错，首先，课程代表结点，课程与课程的联系代表边，我们用一个graph来存储每个课程的入度，例如graph[i]存放的是与course i有边的course，然后我们用inDegree来存放每个结点的入度。然后我们用队列先把入度为0的结点存起来，然后依次取出，队列中的值，对每个结点与只相关的边，我们都要-1，然后又重新把度为0的加入队列，直至队列为空位置。

如果队列便利完，还有结点入度>0，则存在环。

# reference

[[LeetCode] Course Schedule 课程清单][1]

[1]: https://www.cnblogs.com/grandyang/p/4484571.html