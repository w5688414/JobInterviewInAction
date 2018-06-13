# problem
>Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Example 1:
```
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```
Example 2:
```
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```
Note:
1. The input string length won't exceed 1000.


# codes
```
class Solution {
public:
    int countSubstrings(string s) {
        if(s.empty()) return 0;
        int count=0;
        for(int i=0;i<s.length();i++){
            helper(s,i,i,count);
            helper(s,i,i+1,count);
        }
        return count;
    }
private:
    void helper(string s,int i,int j,int &count){
        while(i>=0&&j<s.length()&&(s[i]==s[j])){
            i--;
            j++;
            count++;
        }
    }
};
```

# analysis
>这是暴力的解法，就是把string的每一个位置当作回文子串的中心位置串，如果回文子串长度为奇数是，中间位置只有一个i；如果回文子串为偶数时，中间未知就为i,i+1;然后向两边拓展，这样遍历完以后就能得到所有的情况。

# reference
[[LeetCode] Palindromic Substrings 回文子字符串][1]

[1]: https://www.cnblogs.com/grandyang/p/7404777.html
