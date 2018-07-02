# problem
> Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given"25525511135",

return["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# codes

## s1
```
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        string t;
        DFS(result,t,s,0);
        return result;
        
    }
    void DFS(vector<string> &result, string t, string s, int count){
        if(count==3&&isValid(s)){
            result.push_back(t+s);
            return ;
        }
        for(int i=1;i<4&&i<s.size();i++){
            string sub=s.substr(0,i);
            if(isValid(sub)){
                DFS(result,t+sub+".",s.substr(i),count+1);
            }
        }
    }
    
    bool isValid(string &s){
        int num=atoi(s.c_str());
        if(s.size()>1){
            return num>=0&&num<=255&&s[0]!='0';
        }
        return num>=0&&num<=255;
    }
};

```
## s2
```
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        string out="";
        solve(s,4,out,res);
        return res;
    }
    
    void solve(string s,int k,string out,vector<string> &res){
        if(k==0){
            if(s.empty()){
                res.push_back(out);
            }
            return ;
        }
        for(int i=1;i<4;i++){
            if(s.size()>=i&&isValid(s.substr(0,i))){
                if(k==1) solve(s.substr(i),k-1,out+s.substr(0,i),res);
                else solve(s.substr(i),k-1,out+s.substr(0,i)+'.',res);
            }
        }
        
    }
    bool isValid(string s){
        if(s.empty()||s.size()>3||(s.size()>1&&s[0]=='0')){
            return false;
        }
        int res=atoi(s.c_str());
        return res<=255&&res>=0;
    }
};
```


# analysis
## s1
>没什么说的，深度优先搜索。
## s2
虽然dfs写了很多，但是这个我觉得写起来有点困难，毕竟加了很多东西。

一是只要遇到字符串的子序列或配准问题首先考虑动态规划DP，二是只要遇到需要求出所有可能情况首先考虑用递归。

这道题并非是求字符串的子序列或配准问题，更符合第二种情况，所以我们要用递归来解。我们用k来表示当前还需要分的段数，如果k = 0，则表示三个点已经加入完成，四段已经形成，若这时字符串刚好为空，则将当前分好的结果保存。若k != 0, 则对于每一段，我们分别用一位，两位，三位来尝试，分别判断其合不合法，如果合法，则调用递归继续分剩下的字符串，最终和求出所有合法组合

# reference
[[编程题]restore-ip-addresses][1]
[[LeetCode] Restore IP Addresses 复原IP地址][2]

[1]: https://www.nowcoder.com/questionTerminal/ce73540d47374dbe85b3125f57727e1e
[2]: http://www.cnblogs.com/grandyang/p/4305572.html