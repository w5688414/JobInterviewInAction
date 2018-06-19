# problem
>Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
Example 1:
```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```
Example 2:
```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

# codes
```
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        if(s.empty()) return {};
        vector<int> result;
        vector<int> cnt(128,0);
        for(char c:p){
            cnt[c]++;
        }
        for(int i=0;i<s.size();i++){
            vector<int> temp=cnt;
            bool success=true;
            for(int j=i;j<i+p.size();j++){
                if(temp[s[j]]>0){
                    temp[s[j]]--;
                }else{
                    success=false;
                    break;
                }
            }
            if(success){
                result.push_back(i);
            }
        }
        return result;
    }
};
```

# analysis
>首先统计字符串p中字符出现的次数，然后从s的开头开始，每次找p字符串长度个字符，来验证字符个数是否相同，如果不相同出现了直接break，如果一直都相同了，则将起始位置加入结果res中

# reference
[[LeetCode] Find All Anagrams in a String 找出字符串中所有的变位词][1]

[1]: https://www.cnblogs.com/grandyang/p/6014408.html