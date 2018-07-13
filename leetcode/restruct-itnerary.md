# problem
> Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

1. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
2. All airports are represented by three capital letters (IATA code).
3. You may assume all tickets form at least one valid itinerary.

Example 1:
```
Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
```
Example 2:
```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
```

# codes

## s1
```
class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        vector<string> res;
        unordered_map<string,multiset<string>> m;
        for(auto a:tickets){
            m[a.first].insert(a.second);
        }
        solve(m,"JFK",res);
        return vector<string>(res.rbegin(),res.rend());
    }
    void solve(unordered_map<string,multiset<string>>& m,string s,vector<string>& res){
        while(m[s].size()){
            string t=*m[s].begin();
            m[s].erase(m[s].begin());
            solve(m,t,res);
        }
        res.push_back(s);
    }
};

```


# analysis
## s1
>set不允许重复，multiset就允许重复了，这个函数不会用，所以就不会了好吧，我傻。

# reference
[[LeetCode] Reconstruct Itinerary 重建行程单][1]

[1]: https://www.cnblogs.com/grandyang/p/5183210.html