There are a total of n courses you have to take, labeled from 0 to n-1.

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

1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
2. You may assume that there are no duplicate edges in the input prerequisites.

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

# reference
[]