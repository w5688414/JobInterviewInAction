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
    
    void dfs(string s,vector<vector<string>> &result, vector<string> &path){
        if(s.size()<1){
            result.push_back(path);
            return ;
        }
        for(int i=0;i<s.size();i++){
            int begin=0;
            int end=i;
            while(begin<end){
                if(s[begin]==s[end]){
                    begin++;
                    end--;
                }else{
                    break;
                }
            }
            if(begin>=end){
                path.push_back(s.substr(0,i+1));
                dfs(s.substr(i+1,s.size()),result,path);
                path.pop_back();
            }
        }
        
    }
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> path;
        dfs(s,result,path);
        return result;
    }
};

```

# analysis
>如果是输出所有可能的状态的话，就要用到深度优先搜索，截取一个子串，然后判断是否为回文子串，如果是，加入path表中，然后深度继续寻找。
# reference
[[编程题]palindrome-partitioning][1]

[1]: https://www.nowcoder.com/questionTerminal/f983806a2ecb4106a17a365a642a9632