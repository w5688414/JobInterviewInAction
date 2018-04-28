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

# analysis
- 


# reference
[[编程题]letter-combinations-of-a-phone-number][1]

[1]: https://www.nowcoder.com/questionTerminal/5044a44afe6c40ec9b67b7531393e854