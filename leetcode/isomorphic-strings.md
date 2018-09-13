# problem
>Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
```
Input: s = "egg", t = "add"
Output: true
```
Example 2:
```
Input: s = "foo", t = "bar"
Output: false
```
Example 3:
```
Input: s = "paper", t = "title"
Output: true
```
Note:
You may assume both s and t have the same length.

# codes

## s1
```
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char,char> res,st;
        for(int i=0;i<s.length();i++){
            if(res.count(s[i])||st.count(t[i])){
                if(res[s[i]]!=t[i]||st[t[i]]!=s[i]){
                    return false;
                }
            }else{
                res[s[i]]=t[i];
                st[t[i]]=s[i];
            }
        }
        return true;
    }
};
```

## s2
```
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int m1[256] = {0}, m2[256] = {0}, n = s.size();
        for (int i = 0; i < n; ++i) {
            if (m1[s[i]] != m2[t[i]]) return false;
            m1[s[i]] = i + 1;
            m2[t[i]] = i + 1;
        }
        return true;
    }
};
```



# analysis
## s1

>我自己用的两个hash表来做的。
## s2
下面是hash表
两个哈希表分别来记录原字符串和目标字符串中字符出现情况，由于ASCII码只有256个字符，所以我们可以用一个256大小的数组来代替哈希表，并初始化为0，我们遍历原字符串，分别从源字符串和目标字符串取出一个字符，然后分别在两个哈希表中查找其值，若不相等，则返回false，若相等，将其值更新为i + 1，因为默认的值是0，所以我们更新值为i + 1，这样当 i=0 时，则映射为1，如果不加1的话，那么就无法区分是否更新了
# reference
[[LeetCode] Isomorphic Strings 同构字符串][1]

[1]: https://www.cnblogs.com/grandyang/p/4465779.html
