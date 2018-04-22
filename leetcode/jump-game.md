# problem
>Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A =[2,3,1,1,4], returntrue.

A =[3,2,1,0,4], returnfalse.

# codes
```
class Solution {
public:
    bool canJump(int A[], int n) {
        int max_val=0; //max_val标记能跳到的最远处。
        for(int i=0;i<n&&i<=max_val;i++){ //max_val>=i表示此时能跳到i处，0<=i<n表
            max_val=max(max_val,A[i]+i);  //示扫描所有能到达的点，在改点处能跳到的最远处。
        }
        if(max_val<n-1){ //如果最后跳的最远的结果大于等于n-1，那么满足,能跳到最后，否则，不能。
            return false;
        }
        return true;
    }
  
};

```

# analysis
>分析见注释


# reference
[[编程题]jump-game][1]

[1]: https://www.nowcoder.com/questionTerminal/a2d856f493424a748bb7c9c1126e8d8d