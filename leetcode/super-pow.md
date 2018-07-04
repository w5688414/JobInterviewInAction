# problem
>Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:
```
a = 2
b = [3]

Result: 8
```
Example 2:
```
a = 2
b = [1,0]

Result: 1024
```

# codes
```
class Solution {
public:
    int superPow(int a, vector<int>& b) {
        long long res=1;
        for(int i=0;i<b.size();i++){
            res=pow(res,10)*pow(a,b[i])%1337;
        }
        return res;
    }
    int pow(int x,int n){
        if(n==0) return 1;
        if(n==1) return x%1337;
        return pow(x%1337,n/2)*pow(x%1337,n-n/2)%1337;
    }
};
```

# analysis
>先序遍历每个结点，用一个sum变量保存求和的值，每一层都比上层和*10+当前根节点的值。
比如223 = (22)10 * 23, 所以我们可以从b的最高位开始，算出个结果存入res，然后到下一位是，res的十次方再乘以a的该位次方再对1337取余

# reference
[[LeetCode] Super Pow 超级次方][1]

[1]: https://www.cnblogs.com/grandyang/p/5651982.html
