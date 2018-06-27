# problem
>Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s ="aab",
Return
```
 [
    ["aa","b"],
    ["a","a","b"]
  ]
```

# codes
```
class Solution {
    
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> out;
        dfs(s,0,out,res);
        return res;
    }
    
    void dfs(string s,int start,vector<string> &out,vector<vector<string>>&res){
        if(start==s.size()){
            res.push_back(out);
            return;
        }
        for(int i=start;i<s.length();i++){
            if(isPalindrome(s,start,i)){
                out.push_back(s.substr(start,i-start+1));
                dfs(s,i+1,out,res);
                out.pop_back();
            }
        }
    }
    
    bool isPalindrome(string s,int start,int end){
        while(start<end){
            if(s[start]!=s[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};
```

# analysis
>如果是输出所有可能的状态的话，就要用到深度优先搜索，截取一个子串，然后判断是否为回文子串，如果是，加入path表中，然后深度继续寻找。

# reference
[[编程题]palindrome-partitioning][1]
[[LeetCode] Palindrome Partitioning 拆分回文串][2]

[1]: https://www.nowcoder.com/questionTerminal/f983806a2ecb4106a17a365a642a9632
[2]: http://www.cnblogs.com/grandyang/p/4270008.html