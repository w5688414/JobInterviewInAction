# problem
>For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format. 

Example 1:
```
Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.
```
Example 2:
```
Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
```
Example 3:
```
Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
```
Note:
1. The range of n is [3, 10^18].
2. The string representing n is always valid and will not have leading zeros.

# codes
```
class Solution {
public:
    string smallestGoodBase(string n) {
        long long num=stol(n);
        for(int i=log(num+1)/log(2);i>=2;i--){
            long long left=2,right=pow(num,1.0/(i-1))+1;
            while(left<right){
                long long mid=(left+right)/2;
                long sum=0;
                for(int j=0;j<i;j++){
                    sum=sum*mid+1;
                }
                if(sum==num) return to_string(mid);
                else if(sum<num) left=mid+1;
                else right=mid;
            }
        }
        return to_string(num-1);
    }
};
```

# analysis
>如果我们用k表示基数，m表示转为全1数字的位数，那么数字n就可以拆分为：

n = 1 + k + k^2 + k^3 + ... + k^(m-1)

公式求和：  n = (k^m - 1) / (k - 1)

- 我们的目标是求最小的k，那么仔细观察这个式子，在n恒定的情况，k越小则m却大，那么就是说上面的等式越长越好
- 下面我们来分析m的取值范围，题目中给了n的范围，是[3, 10^18]。那么由于k至少为2，n至少为3，那么肯定至少有两项，则m>=2。那么m的上限该如何求？k最小是2，那么m最大只能为log2(n + 1)。
- 我们看题目中最后一个例子，可以发现，当k=n-1时，一定能变成11，所以实在找不到更小的情况下就返回n-1。

没什么好说的，这道题不看答案怎么也不会，我只欣赏一下数学之美。

# reference
[[LeetCode] Smallest Good Base 最小的好基数][1]

[1]: http://www.cnblogs.com/grandyang/p/6620351.html