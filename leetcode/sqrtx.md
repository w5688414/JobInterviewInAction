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

```
class Solution {
public:
    int mySqrt(int x) {
        int i=1;
        while(i*i<=x){
            i++;
            if(i*i<0){
                break;
            }
        }
        return i-1;
    }
};
```

# analysis
1. 第一种：这里求平方根，需要考虑两数相乘溢出的情况。主要思想是用了二分法。
2. 第二种方式就是瞎找了，当然要考虑数据溢出的情况。
3. 第三种是牛顿迭代法，以后遇见了再试。

# reference
[[编程题]sqrtx][1]
[[LeetCode] Sqrt(x) 求平方根][2]

[1]: https://www.nowcoder.com/questionTerminal/09fbfb16140b40499951f55113f2166c
[2]: http://www.cnblogs.com/grandyang/p/4346413.html