# problem
>Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
```
Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
```
Note:

- S will be a string with length at most 12.
- S will consist only of letters or digits.

# codes

```
class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        vector<string> res;
        solve(res,S,0);
        return res;
    }
    void solve(vector<string>& res,string& S,int start){
        if(start==S.size()){
            res.push_back(S);
            return;
        }
        solve(res,S,start+1);
        if(S[start]>'9'){
            S[start]^=32;
            solve(res,S,start+1);
        }
    }
};
```

# analysis
- 看来这不是前面的回溯的问题，是一个深度优先搜索，好吧，我又套公式了。

# reference
[[LeetCode] Letter Case Permutation 字母大小写全排列][1]

[1]: http://www.cnblogs.com/grandyang/p/9065702.html