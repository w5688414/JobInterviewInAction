# problem
>Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Note:
- Only the space character ' ' is considered as whitespace character.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
```
Input: "42"
Output: 42
```
Example 2:
```
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```
Example 3:
```
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```
Example 4:
```
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
```
Example 5:
```
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

```

# codes
```
class Solution {
public:
    int myAtoi(string str) {
        if(str.empty()){
            return 0;
        }
        int i=0;
        while(str[i]==' '){
            i++;
        }
        int sign=1;
        if(str[i]=='-'){
            sign=-1;
            i++;
        }else if(str[i]=='+'){
            i++;
        }
        long sum=0;
        while(str[i]!='\0'&&(str[i]>='0'&&str[i]<='9')){
            sum=sum*10+str[i]-'0';
            if(sum>INT_MAX&&sign==-1){
                return INT_MIN;
            }else if(sum>INT_MAX){
                return INT_MAX;
            }
            i++;
        }
        return (int)sign*sum;
    }
};
```

# analysis
>直接法计算，这里要考虑溢出，有空格，非法字符等情况。我今天又重新做了一次，发现写的代码比以前的好，所以更新了一下代码。

# reference
[[编程题]string-to-integer-atoi][1]
[[LeetCode] String to Integer (atoi) 字符串转为整数][2]

[1]: https://www.nowcoder.com/questionTerminal/44d8c152c38f43a1b10e168018dcc13f
[2]: http://www.cnblogs.com/grandyang/p/4125537.html
