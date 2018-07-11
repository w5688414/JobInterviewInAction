# problem
>Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
```
Input: N = 10
Output: 9
```
Example 2:
```
Input: N = 1234
Output: 1234
```
Example 3:
```
Input: N = 332
Output: 299
```
Note: N is an integer in the range [0, 10^9].

# codes
```
class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        string s=to_string(N);
        int n=s.size();
        int j=n;
        for(int i=n-1;i>0;i--){
            if(s[i]>=s[i-1]) continue;
            s[i-1]--;
            j=i;
        }
        for(int i=j;i<n;i++){
            s[i]='9';
        }
        return stoi(s);
    }
};
```

# analysis
>从后往前遍历的最后一个值升高的位置，让前一位减1，并把当前位以及后面的所有位都变成9，就可以得到最大的单调递增数啦。

# reference
[[LeetCode] Monotone Increasing Digits 单调递增数字][1]

[1]: http://www.cnblogs.com/grandyang/p/8068326.html