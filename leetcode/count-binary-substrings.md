# problem
>Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
```
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
```
Example 2:
```
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
```

Note:
- s.length will be between 1 and 50,000.
- s will only consist of "0" or "1" characters.

# codes
```
class Solution {
public:
    int countBinarySubstrings(string s) {
        int zeros=0;
        int ones=0;
        int res=0;
        for(int i=0;i<s.length();i++){
            if(i==0){
                s[i]=='1' ? ones++:zeros++;
            }else{
                if(s[i]=='1'){
                    ones= s[i-1]=='1' ? ones+1:1;
                    if(zeros>=ones){
                        res++;
                    }
                }else{
                    zeros= s[i-1]=='0' ? zeros+1:1;
                    if(ones>=zeros){
                        res++;
                    }
                }
            }
        }
        return res;
    }
};
```

# analysis
>
- 我们来分析题目中的第一个例子00110011，符合要求的子字符串要求0和1同时出现，那么当第一个1出现的时候，前面由于前面有两个0，所以肯定能组成01，再遇到下一个1时，此时1有2个，0有2个，能组成0011，下一个遇到0时，此时0的个数重置为1，而1的个数有两个，所以一定有10，同理，下一个还为0，就会有1100存在，之后的也是这样分析。

- 那么我们可以发现我们只要分别统计0和1的个数，而且如果当前遇到的是1，那么只要之前统计的0的个数大于当前1的个数，就一定有一个对应的子字符串，而一旦前一个数字和当前的数字不一样的时候，那么当前数字的计数要重置为1。所以我们遍历元数组，如果是第一个数字，那么对应的ones或zeros自增1。然后进行分情况讨论，如果当前数字是1，然后判断如果前面的数字也是1，则ones自增1，否则ones重置为1。如果此时zeros大于ones，res自增1。反之同理，如果当前数字是0，然后判断如果前面的数字也是0，则zeros自增1，否则zeros重置为1。如果此时ones大于zeros，res自增1。

# reference

[[LeetCode] Count Binary Substrings 统计二进制子字符串][1]

[1]: http://www.cnblogs.com/grandyang/p/7716150.html
