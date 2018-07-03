# problem
>Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:
```
Input: S = "aab"
Output: "aba"
```
Example 2:
```
Input: S = "aaab"
Output: ""
```

# codes
```
class Solution {
public:
    string reorganizeString(string S) {
        int cnt=0;
        int n=S.size();
        string res;
        unordered_map<char,int> m;
        priority_queue<pair<int,char>> q;
        for(auto s:S){
            m[s]++;
        }
        for(auto a:m){
            if(a.second>((n+1)/2)) return "";
            q.push({a.second,a.first});
        }
        while(q.size()>=2){
            auto t1=q.top(); q.pop();
            auto t2=q.top(); q.pop();
            res.push_back(t1.second);
            res.push_back(t2.second);
            if(--t1.first>0) q.push(t1);
            if(--t2.first>0) q.push(t2);
        }
        if(q.size()>0) res.push_back(q.top().second);
        return res;
    }
};
```

# analysis
>先用hashmap统计词频，然后用priority queue把hashmap的健值对反过来建立最大堆，每次取出两个字符，然后词频-1放入优先级队列中，这样重复直到队列里面的的元素为空为止。思路就是这个，我怎么也不会想到用优先级队列办事情的，看来我还是太肤浅了，加油。

# reference
[[LeetCode] Reorganize String 重构字符串][1]

[1]: http://www.cnblogs.com/grandyang/p/8799483.html