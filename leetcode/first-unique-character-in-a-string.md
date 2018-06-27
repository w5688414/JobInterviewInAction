# problem
>Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:
```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```
Note: You may assume the string contain only lowercase letters.


# codes
```
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char,int> m;
        for(auto c:s){
            m[c]++;
        }
        for(int i=0;i<s.size();i++){
            if(m[s[i]]==1){
                return i;
            }
        }
        return -1;
    }
};
```

# analysis
>我虽然想到了用hash表统计词频，但是没想到怎么把顺序解决，看来还是稚嫩了一点，需要多锻炼。

# reference
[[LeetCode] First Unique Character in a String 字符串第一个不同字符][1]
[1]: http://www.cnblogs.com/grandyang/p/5802109.html