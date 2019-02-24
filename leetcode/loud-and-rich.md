# problem
>In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label x, simply "person x".

We'll say that richer[i] = [x, y] if person x definitely has more money than person y.  Note that richer may only be a subset of valid observations.

Also, we'll say quiet[x] = q if person x has quietness q.

Now, return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]), among all people who definitely have equal to or more money than person x.

Example 1:
```
Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation: 
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.
```
Note:

1. 1 <= quiet.length = N <= 500
2. 0 <= quiet[i] < N, all quiet[i] are different.
3. 0 <= richer.length <= N * (N-1) / 2
4. 0 <= richer[i][j] < N
5. richer[i][0] != richer[i][1]
6. richer[i]'s are all different.
7. The observations in richer are all logically consistent.

# codes
```
class Solution {
public:
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        int n=quiet.size();
        vector<vector<int>> graph(n);
        vector<int> res(n,-1);
        for(auto edge:richer){
            graph[edge[1]].push_back(edge[0]);
        }
        for(int i=0;i<n;i++){
            dfs(graph,res,i,quiet);
        }
        return res;
    }
    int dfs(vector<vector<int>>& graph,vector<int>& res,int i,vector<int>& quiet){
        if(res[i]==-1){
            res[i]=i;
            for(auto child:graph[i]){
                int cand=dfs(graph,res,child,quiet);
                if(quiet[cand]<quiet[res[i]]){
                    res[i]=cand;
                }
            }
        }
        return res[i];
    }
};
```

# analysis
题目的意思是：给出了有钱人之间的对比，在richer中第一个数字的人比第二个数字的人有钱。quiet值代表每个人的安静指数，数字越大代表越吵。现在要找出对于每个人，比他有钱的人还比他安静是谁。
- 看懂题目以后，就会发现就是一个图的遍历。
- 把这个过程看称是一个图，x当作节点，richer[i] = [x, y] 当作边，其中x为一条边的右边的结点，y为一条边的左边的结点，图为有向图，DFS遍历有向图，如果发现得到的quiet比当前的小，则更新res的least quiet。最终得到的是least quietness。


# reference
[851. Loud and Rich][1]

[1]: https://leetcode.com/problems/loud-and-rich/solution/
