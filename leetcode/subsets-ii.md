# problem
>Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

For example,
If S =[1,2,2], a solution is:
```
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```
# codes
```
class Solution {
private:
    vector<vector<int> > result;
    vector<int> ans;
public:
    vector<vector<int> > subsetsWithDup(vector<int> &S) {
        sort(S.begin(),S.end());
        dfs(S,0);
        return result;
    }
    void dfs(vector<int> S,int start){
        result.push_back(ans);
        for(int i=start;i<S.size();i++){
            ans.push_back(S[i]);
            dfs(S,i+1);
            while(i<S.size()-1&&S[i+1]==S[i]){
                ++i;
            }
            ans.pop_back();
        }
    }
};

```

# analysis
>看完了思路还是蛮简单的，就是一个深度优先搜索，先对vector进行排序，如果在遍历的时候，遇见重复的，则需要跳过去。
# reference
[[编程题]subsets-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/66cf0498e9fd4730ab453dac978bf7e6
