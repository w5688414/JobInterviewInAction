# problem
> You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
```
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
```
Example 2:
```
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
```
Note:
- target will be a non-zero integer in the range [-10^9, 10^9].

# codes
```
class Solution {
public:
    int reachNumber(int target) {
        target=abs(target);
        int sum=0;
        int i;
        for(i=1;sum<target;i++){
            sum+=i;
        }
        i--;
        if((sum-target)%2==0){
            return i;
        }else{
            if(i%2==0) return i+1;
            else return i+2;
        }
    }
};
```

# analysis
- 首先，要到达目的地一定会有向左和向右，我们假设一定有一个最好的方案，a1,a2,a3…an,假如a1到an都是正数，那么它一定是最好的方案，假如存在负数，那么可以看成把a1,a2…an里面的若干个数变成负数，然后到达target.
- 可以证明，当a1+a2..an-target为偶数的时候，只需要把a1,a2,…an里面的一个数变成负数就能到达目的地，这就是最好的方案.
- 当a1+a2..an-target为奇数的时候,有两种情况，当n为偶数的时候，n+1为奇数，可以证明，当把a1,a2..an里面一个数变成负数之后，只要在加一个数就能到达target，也就是a1+a2…an+an+1一定可以到达target,当n为奇数的时候，可以证明当把a1,a2..an里面一个数变成负数之后只要在加两个数就能到达target，也就是a1+a2…an+an+1+an+2

这道题既不会证明也不会写代码，欣赏一下吧。

# reference
[LeetCode | 754. Reach a Number 数学原理题解析与证明][1]


[1]: https://blog.csdn.net/u012737193/article/details/78951070