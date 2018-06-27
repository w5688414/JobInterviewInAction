# problem
>Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```
Example 2:
```
Input: s = "rat", t = "car"
Output: false
```
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

# codes
```
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()){
            return false;
        }
        vector<int> v(26,0);
        for(int i=0;i<s.length();i++){
            v[s[i]-'a']++;
        }
        for(int j=0;j<t.length();j++){
            v[t[j]-'a']--;
            if(v[t[j]-'a']<0){
                return false;
            }
        }
        return true;
    }
};
```

# analysis
>这道题我想的是hash表的方式，然后这个解法是用了一个大小为26的一维数组，统计每个字符的频率就行了。

# reference
[[LeetCode] Valid Anagram 验证变位词][1]
[1]: http://www.cnblogs.com/grandyang/p/4694988.html