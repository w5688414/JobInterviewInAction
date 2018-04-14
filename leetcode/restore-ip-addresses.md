# problem
> Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given"25525511135",

return["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# codes
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

# analysis
>没什么说的，深度优先搜索。
# reference
[[编程题]restore-ip-addresses][1]

[1]: https://www.nowcoder.com/questionTerminal/ce73540d47374dbe85b3125f57727e1e
