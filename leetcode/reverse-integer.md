# problem
> Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
```
Input: 123
Output: 321
```
Example 2:
```
Input: -123
Output: -321
```
Example 3:
```
Input: 120
Output: 21
```
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# codes
```
class Solution {
public:
    int reverse(int x) {
        int res=0;
        while(x!=0){
            if(abs(res)>INT_MAX/10){
                return 0;
            }
            res=res*10+x%10;
            x=x/10;
        }
     
        return res ;
    }
};
```

# analysis
>我虽然写了一份代码，但是不简洁，我感觉这份代码很好，不过还没弄明白为啥INT_MAX/10，好吧，好像也AC了，以后再看吧。

# reference
[[LeetCode] Reverse Integer 翻转整数][1]

[1]: http://www.cnblogs.com/grandyang/p/4125588.html
