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
>我虽然写了一个版本，但是并不高效，这里用了双指针法，学习一下。使用两个哈希表来做，或者是使用一个哈希表配上双指针来做。我们先来看使用两个哈希表来做的情况，我们先来分别统计s1和s2中前n1个字符串中各个字符出现的次数，其中n1为字符串s1的长度，这样如果二者字符出现次数的情况完全相同，说明s1和s2中前n1的字符互为全排列关系，那么符合题意了，直接返回true。如果不是的话，那么我们遍历s2之后的字符，对于遍历到的字符，对应的次数加1，由于窗口的大小限定为了n1，所以每在窗口右侧加一个新字符的同时就要在窗口左侧去掉一个字符，每次都比较一下两个哈希表的情况，如果相等，说明存在，

## reference
[[LeetCode] Permutation in String 字符串中的全排列][1]


[1]: http://www.cnblogs.com/grandyang/p/6815227.html