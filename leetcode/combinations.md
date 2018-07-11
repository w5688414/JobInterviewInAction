# problem
>Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

```
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```
# codes
## s1
```
class Solution {
private:
    vector<vector<int> > result;
    vector<int> ans;
public:
    vector<vector<int> > combine(int n, int k) {
        if(k)
        dfs(n,k,1);
        return result;
    }
    void dfs(int n,int k,int start ){
        if(k<0){
            return;
        }else if(k==0){
            result.push_back(ans);
        }else{
            for(int i=start;i<=n;i++){
                ans.push_back(i);
                dfs(n,k-1,start+1);
                ans.pop_back();
            }            
        }

    }
};
```
## s2
```
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> out;
        solve(res,out,n,k,1);
        return res;
    }
    void solve(vector<vector<int>>& res,vector<int> out,int n,int k,int start){
        if(k==0||start>n){
            if(k==0) res.push_back(out);
            return;
        }
        for(int i=start;i<=n;i++){
            out.push_back(i);
            solve(res,out,n,k-1,i+1);
            out.pop_back();
        }
    }
};
```

# analysis
>回溯法，虽然模式是固定的，但是让我调试的好辛苦。
## s2
 重写了一遍，感觉比以前写的更好了，所以覆盖了原有的解法。

# reference
[手把手教你<leetcode>中的回溯算法——多一点套路][1]
[[编程题]combinations][2]

[1]: https://blog.csdn.net/versencoder/article/details/52071930
[2]: https://www.nowcoder.com/questionTerminal/4d0a110416d84c7f9454d0da53ab2da1