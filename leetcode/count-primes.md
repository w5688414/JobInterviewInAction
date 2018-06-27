# problem
>Count the number of prime numbers less than a non-negative number, n.

Example:
```
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```

# codes
```
class Solution {
public:
    int countPrimes(int n) {
        vector<bool> num(n-1,true);
        num[0]=false;
        int res=0;
        int limit=sqrt(n);
        for(int i=2;i<=limit;i++){
            if(num[i-1]){
                for(int j=i*i;j<n;j+=i){
                    num[j-1]=false;
                }
            }
        }
        for(int i=0;i<n-1;i++){
            if(num[i]){
                res++;
            }
        }
        return res;
    }
};
```

# analysis
>我们从2开始遍历到根号n，先找到第一个质数2，然后将其所有的倍数全部标记出来，然后到下一个质数3，标记其所有倍数，一次类推，直到根号n，此时数组中未被标记的数字就是质数。我们需要一个n-1长度的bool型数组来记录每个数字是否被标记，长度为n-1的原因是题目说是小于n的质数个数，并不包括n。

# reference

[[LeetCode] Count Primes 质数的个数][1]


[1]: http://www.cnblogs.com/grandyang/p/4462810.html