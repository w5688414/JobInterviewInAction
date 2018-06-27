# problem
>Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:
```
Input: ["flower","flow","flight"]
Output: "fl"
```
Example 2:
```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```
Note:

All given inputs are in lowercase letters a-z.

# codes

## s1
```
//先对字符串排序，然后考虑第一个和最后一个的首字符，这两个字符必定是差距最大的两个
//(因为排序首先从第一个开始排)，如果这两个不等，就返回空，否则，说明所有字符串的首
//字符相等，那么接着判断第二个。
class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if(strs.size()==0){
            return "";
        }
        sort(strs.begin(),strs.end());
        int len=strs.size();
        int l=min(strs[0].size(),strs[len-1].size());
        for(int i=0;i<l;i++){
            if(strs[0][i]!=strs[len-1][i]){
                return strs[0].substr(0,i);
            }
        }
        return strs[0];
    }
};
```
## s2
```
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==0||strs[0].size()==0){
            return "";
        }
        string res="";
        int m=strs.size();
        int n=strs[0].size();
        for(int j=0;j<n;j++){
            char ch=strs[0][j];
            for(int i=1;i<m;i++){
                if(j>=strs[i].size()||strs[i][j]!=ch){
                    return res;
                }
            }
            res.push_back(ch);
        }
        return res;
    }
};
```

# analysis
>先对字符串进行排序，这样差距最大的两个字符串必定是排在第一排和最后一排，我们只需要判断第一排和最后一排饿最长公共字符串就行了。
## s2
一列一列的比较，没啥说的，这是最暴力的方法了。

# reference
[[编程题]longest-common-prefix][1]
[[LeetCode] Longest Common Prefix 最长共同前缀][2]

[1]: https://www.nowcoder.com/questionTerminal/28eb3175488f4434a4a6207f6f484f47
[2]: http://www.cnblogs.com/grandyang/p/4606926.html
