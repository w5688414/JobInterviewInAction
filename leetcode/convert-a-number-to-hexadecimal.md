# problem
>Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

1. All letters in hexadecimal (a-f) must be in lowercase.
2. The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
3. The given number is guaranteed to fit within the range of a 32-bit signed integer.
4. You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:
```
Input:
26

Output:
"1a"
```
Example 2:
```
Input:
-1

Output:
"ffffffff"
```
# codes
```
class Solution {
public:
    string toHex(int num) {
        string res;
        for(int i=0;num&&i<8;i++){
            int t=num&0xf;
            if(t>=10) res=char('a'+t-10)+res;
            else res=char('0'+t)+res;
            num>>=4;
        }
        return res.empty() ? "0":res;
    }
};
```

# analysis
>我们采取位操作的思路，每次取出最右边四位，如果其大于等于10，找到对应的字母加入结果，反之则将对应的数字加入结果，然后num像右平移四位，循环停止的条件是num为0，或者是已经循环了7次.

# reference
[[LeetCode] Convert a Number to Hexadecimal 数字转为十六进制][1]

[1]: http://www.cnblogs.com/grandyang/p/5926674.html