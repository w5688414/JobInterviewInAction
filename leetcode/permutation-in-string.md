# problem
>Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
```
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
```
Example 2:
```
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```
Note:
1. The input strings only contain lower case letters.
2. The length of both given strings is in range [1, 10,000].

# codes

```
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1=s1.size();
        int n2=s2.size();
        int left=0;
        vector<int> m(128);
        for(char ch:s1) ++m[ch];
        for(int right=0;right<n2;right++){
            m[s2[right]]--;
            if(m[s2[right]]<0){ 
                while (++m[s2[left++]] != 0) {}
            }else if(right-left+1==n1) return true;
        }
        return n1==0;
    }
};
```
# analysis
>我虽然写了一个版本，但是并不高效，这里用了双指针法，学习一下。

## reference
[[LeetCode] Permutation in String 字符串中的全排列][1]


[1]: http://www.cnblogs.com/grandyang/p/6815227.html