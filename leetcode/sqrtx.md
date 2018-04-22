# problem
>Implementint sqrt(int x).

Compute and return the square root of x.

# codes
```
class Solution {
public:
    int sqrt(int x) {
        if(x<2){
            return x;
        }
        int low=1;
        int high=x/2;
        int mid=0;
        while(low<=high){
            mid=(high+low)/2;
            if(x/mid>mid){
                low=mid+1;
            }else if(x/mid==mid){ //不用x > mid * mid 会溢出
                return mid;
            }
            else{
                high=mid-1;
            }
        }
        if(x/mid<mid){
            return mid-1;
        }
        return mid;
    }
};

```

# analysis
>这里求平方根，需要考虑两数相乘溢出的情况。主要思想是用了二分法。

# reference
[[编程题]sqrtx][1]

[1]: https://www.nowcoder.com/questionTerminal/09fbfb16140b40499951f55113f2166c
