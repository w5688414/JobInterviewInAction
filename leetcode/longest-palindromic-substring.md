# problem
>Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
Example 2:
```
Input: "cbbd"
Output: "bb"
```

# codes
```
class Solution {
public:
    string longestPalindrome(string s) {
        int max_len=0;
        int start=0;
        for(int i=0;i<s.length();i++){
            int left=i-1;
            int right=i+1;
            while(left>=0&&right<s.length()&&s[left]==s[right]){
                int cur_len=right-left;
                if(cur_len>max_len){
                    max_len=cur_len;
                    start=left;
                }
                left--;
                right++;
            }
            
            left=i;
            right=i+1;
            while(left>=0&&right<=s.length()&&s[left]==s[right]){
                int cur_len=right-left;
                if(cur_len>max_len){
                    max_len=cur_len;
                    start=left;
                }
                left--;
                right++;   
            }
        }
        return s.substr(start,max_len+1);
    }
};
```

# analysis
>首先建立一个hash表，然后初始化存储所有的数据元素。遍历数组，然后去找相关的hash表的值，如果找到了，就删除，并且重复遍历其相邻的hash表的值。就行了
# reference
[Manacher's Algorithm 马拉车算法][1]
[LeetCode 5. Longest Palindromic Substring（最长回文连续子串）][2]
[[Leetcode] Longest palindromic substring 最长回文子串][3]
[Longest Palindromic Substring Part II][4]

[1]: http://www.cnblogs.com/grandyang/p/4475985.html
[2]: https://blog.csdn.net/princexiexiaofeng/article/details/79573048
[3]: https://www.cnblogs.com/love-yh/p/7071871.html
[4]: https://articles.leetcode.com/longest-palindromic-substring-part-ii/
