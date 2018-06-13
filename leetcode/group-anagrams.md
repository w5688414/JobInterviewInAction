# problem
>Given an array of strings, group anagrams together.
Example:
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
Note:
- All inputs will be in lowercase.
- The order of your output does not matter.

# codes
```
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        if(strs.empty()){
            return res;
        }
        unordered_map<string,multiset<string>> mp;
        for(string s:strs){
            string temp=s;
            sort(temp.begin(),temp.end());
            mp[temp].insert(s);
        }
        for(auto m:mp){
            vector<string> ans(m.second.begin(),m.second.end());
            res.push_back(ans);
        }
        return res;
    }
};
```

# analysis
>这道题目我没有写出代码的原因是我对C++的multiset和unordered_map不熟，思路上没有什么障碍。非常的简单明了，先用一个map把排序的字符串当作key，把对应的原有的字符串当作value，这样会把相同的key的字符串归类到一起。然后依次遍历这个map就行了。

# reference
[【LeetCode】49. Group Anagrams][1]

[1]: https://www.cnblogs.com/jdneo/p/5291304.html
