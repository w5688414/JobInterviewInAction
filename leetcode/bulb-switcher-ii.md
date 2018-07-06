# problem
>There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

1. Flip all the lights.
2. Flip lights with even numbers.
3. Flip lights with odd numbers.
4. Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...

Example 1:
```
Input: n = 1, m = 1.
Output: 2
Explanation: Status can be: [on], [off]
```
Example 2:
```
Input: n = 2, m = 1.
Output: 3
Explanation: Status can be: [on, off], [off, on], [off, off]
```
Example 3:
```
Input: n = 3, m = 1.
Output: 4
Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
```
Note: n and m both fit in range [0, 1000].

# codes
```
class Solution {
public:
    int flipLights(int n, int m) {
        if(m==0||n==0) return 1;
        if(n==1) return 2;
        if(n==2) return m==1 ? 3:4;
        if(m==1) return 4;
        return m==2 ? 7:8;
    }
};
```

# analysis
>这道题最多只有8中情况(我不知道怎么的出来的)，所以很适合分情况来讨论：

- 当m和n其中有任意一个数是0时，返回1

- 当n = 1时

只有两种情况，0和1

- 当n = 2时，

这时候要看m的次数，如果m = 1，那么有三种状态 00，01，10

当m > 1时，那么有四种状态，00，01，10，11

- 当m = 1时，

此时n至少为3，那么我们有四种状态，000，010，101，011

- 当m = 2时，

此时n至少为3，我们有七种状态：111，101，010，100，000，001，110

- 当m > 2时，

此时n至少为3，我们有八种状态：111，101，010，100，000，001，110，011

# reference
[[LeetCode] Bulb Switcher II 灯泡开关之二][1]

[1]: http://www.cnblogs.com/grandyang/p/7595595.html