# problem
>Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:
```
Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
```
Example 2:
```
Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
```
Example 3:
```
Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
```
Note:1 <= N <= 10 ^ 9.

# codes
```
class Solution {
public:
    int consecutiveNumbersSum(int N) {
        int count=1;
        for(int k=2;k<sqrt(2*N);k++){
            if((N-(k*(k-1)/2))%k==0) count++;
        }
        return count;
    }
};
```

# analysis
>
设 x + (x+1) + (x+2)+...+ k terms = N
kx + k*(k-1)/2 = N
kx = N - k*(k-1)/2

N - k*(k-1)/2 > 0 推出
k*(k-1) < 2N 
这可以近似的用如下式子表示：
k*k < 2N ==> k < sqrt(2N)

说实话，我做不出来，欣赏一下。

# reference
[[LeetCode] Complex Number Multiplication 复数相乘][1]


[1]: http://www.cnblogs.com/grandyang/p/6660437.html