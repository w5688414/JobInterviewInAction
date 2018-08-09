## 拓扑排序
```
class Solution {
public:
    vector<int> topologicalSort(int n, vector<pair<int, int> >& edges) {
        vector<int> res;
        int * in_degree = new int[n];
        queue<int> q;
        for (int i = 0; i < n; i++) {
            in_degree[i] = 0;
        }
        for (int i = 0; i < edges.size(); i++) {
            in_degree[edges[i].second]++;
        }
        for (int i = 0; i < n; i++) {
            if (in_degree[i] == 0) {
                q.push(i);
            }
        }
        while (!q.empty()) {
            int front = q.front();
            q.pop();
            res.push_back(front);
            for (int i = 0; i < edges.size(); i++) {
                if (edges[i].first == front) {
                    in_degree[edges[i].second]--;
                    if (in_degree[edges[i].second] == 0) {
                        q.push(edges[i].second);
                    }
                }
            }
        }
        return res;
    }
}; 
```

# reference
[1]. 拓扑排序（附LeetCode题目）. https://www.cnblogs.com/fengziwei/p/7875355.html