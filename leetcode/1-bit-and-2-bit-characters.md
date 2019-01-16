# problem
>We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
```
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
```
Example 2:
```
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
```
Note:

- 1 <= len(bits) <= 1000.
- bits[i] is always 0 or 1.

# codes
```
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        return solve(bits,0);
    }
    bool solve(vector<int>& bits,int idx){
        int n=bits.size();
        if(idx==n) return false;
        if(idx==n-1) return bits[idx]==0;
        if(bits[idx]==0) return solve(bits,idx+1);
        else return solve(bits,idx+2);
    }
};
```

# analysis
1. 这道题说有两种特殊的字符，一种是两位字符，只能是二进制的11和10，另一种是单个位字符，只能是二进制的0
2. 现在给了我们一个只包含0和1的数组，问我们能否将其正确的分割，使得最后一个字符是个单个位字符

>递归搜索的解法，我觉得这是最容易理解思想的方法，当然也是最暴力的方法啦，把各种终止条件，递归条件写出来就是程序啦。

# reference
[[LeetCode] 1-bit and 2-bit Characters 一位和两位字符][1]

[1]: https://www.cnblogs.com/grandyang/p/7790029.html
