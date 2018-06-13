# problem
>Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
```
Input:Digit string "23" Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
Note: 
Although the above answer is in lexicographical order, your answer could be in any order you want.

# codes
```
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> vec;
        string mp[12]={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        vector<string> ans(1,"");
        for(int i=0;i<digits.size();i++){
            vector<string> tmp;
            for(int j=0;j<ans.size();j++){
                for(int k=0;k<mp[digits[i]-'0'].size();k++){
                    tmp.push_back(ans[j]+mp[digits[i]-'0'][k]);
                }
            }
            ans=tmp;
        }
        return ans;
    }
};
```
```
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if(digits.empty()){
            return res;
        }
        string dict[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        dfs(digits,0,dict,res,"");
        return res;
    }
    void dfs(string digits,int level,string dict[],vector<string> &res,string out){
        if(level==digits.size()){
            res.push_back(out);
        }else{
            string s=dict[digits[level]-'2'];
            for(int i=0;i<s.size();i++){
                out.push_back(s[i]);
                dfs(digits,level+1,dict,res,out);
                out.pop_back();
            }
        }
    }
};
```

# analysis
- 第一种方法我不能理解，虽然我是第一次做的。
第二种方法很直观，就是一个深度优先搜索的问题，我自己在理解关键地方后，做出来了，看来还是分析能力不够，不能一次性的直接求出来。


# reference
[[编程题]letter-combinations-of-a-phone-number][1]
[[LeetCode] Letter Combinations of a Phone Number 电话号码的字母组合][2]

[1]: https://www.nowcoder.com/questionTerminal/5044a44afe6c40ec9b67b7531393e854
[2]: https://www.cnblogs.com/grandyang/p/4452220.html
