# problem
>Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:
```
Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
```


# codes

## s1
```
class Solution {
public:
    int countDigitOne(int n) {
       int res=0;
       int pow10=1;
       int sub=0;
        while(n){
            int div=n%10;
            n=n/10;
            if(div==0) res+=n*pow10;
            else if(div==1) res+=n*pow10+sub+1;
            else if(div>1) res+=(n+1)*pow10;
            sub+=div*pow10;
            pow10*=10;
        }
        return res;
    }
};
```

## s2
```
class Solution {
public:
    int countDigitOne(int n) {
        int res = 0, a = 1, b = 1;
        while (n > 0) {
            res += (n + 8) / 10 * a + (n % 10 == 1) * b;
            b += n % 10 * a;
            a *= 10;
            n /= 10;
        }
        return res;
    }
};
```

# analysis
>这道题我做不出来，也编不出来，比较难。
1的个数          含1的数字                                                                        数字范围

1                   1                                                                                     [1, 9]

11                 10  11  12  13  14  15  16  17  18  19                              [10, 19]

1                   21                                                                                   [20, 29]

1                   31                                                                                   [30, 39]

1                   41                                                                                   [40, 49]

1                   51                                                                                   [50, 59]

1                   61                                                                                   [60, 69]

1                   71                                                                                   [70, 79]

1                   81                                                                                   [80, 89]

1                   91                                                                                   [90, 99]

11                 100  101  102  103  104  105  106  107  108  109          [100, 109]

21                 110  111  112  113  114  115  116  117  118  119             [110, 119]

11                 120  121  122  123  124  125  126  127  128  129          [120, 129]

...                  ...                                                                                  ...

- 100以内的数字，除了10-19之间有11个‘1’之外，其余都只有1个。如果我们不考虑[10, 19]区间上那多出来的10个‘1’的话，那么我们在对任意一个两位数，十位数上的数字(加1)就代表1出现的个数，这时候我们再把多出的10个加上即可。
- 比如56就有(5+1)+10=16个。如何知道是否要加上多出的10个呢，我们就要看十位上的数字是否大于等于2，是的话就要加上多余的10个'1'。那么我们就可以用(x+8)/10来判断一个数是否大于等于2。
- 对于三位数区间 [100, 199] 内的数也是一样，除了[110, 119]之间多出的10个数之外，共21个‘1’，其余的每10个数的区间都只有11个‘1’，所以 [100, 199] 内共有21 + 11 * 9 = 120个‘1’。
- 那么现在想想[0, 999]区间内‘1’的个数怎么求？根据前面的结果，[0, 99] 内共有20个，[100, 199] 内共有120个，而其他每100个数内‘1’的个数也应该符合之前的规律，即也是20个，那么总共就有 120 + 20 * 9 = 300 个‘1’。那么还是可以用相同的方法来判断并累加1的个数，

# reference
[233. Number of Digit One][1]
[[LeetCode] Number of Digit One 数字1的个数][2]

[1]: https://leetcode.com/problems/number-of-digit-one/discuss/137862/C++-solution-with-explanation
[2]: http://www.cnblogs.com/grandyang/p/4629032.html