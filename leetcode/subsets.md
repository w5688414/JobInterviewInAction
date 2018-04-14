# problem
>Given a set of distinct integers, S, return all possible subsets.

Note:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

For example,
If S =[1,2,3], a solution is:

```
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```
# codes
```
class Solution {
private:
    vector<int> ans;
    vector<vector<int> > result;
public:
    vector<vector<int> > subsets(vector<int> &S) {
        sort(S.begin(),S.end());
        for(int i=0;i<=S.size();i++){
            DFS(S,0,i);
        }
        return result;
    }
    
    void DFS(vector<int> &S,int start,int k){
        if(k<0){
            return;
        }
        else if(k==0){
            result.push_back(ans);
        }else{
            for(int i=start;i<S.size();i++){
                ans.push_back(S[i]);
                DFS(S,i+1,k-1);
                ans.pop_back();
            }
        }
    }
};
```

# analysis
>还是一个DFS的题目，看来我是太天真了，需要努力进化。

# reference
[[编程题]subsets][1]

[1]: https://www.nowcoder.com/questionTerminal/c333d551eb6243e0b4d92e37a06fbfc9
