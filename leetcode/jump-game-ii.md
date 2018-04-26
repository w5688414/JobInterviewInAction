# problem
>Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A =[2,3,1,1,4]

The minimum number of jumps to reach the last index is2. (Jump1step from index 0 to 1, then3steps to the last index.)

# codes
```
class Solution {
public:
// 当前能够到达的最远距离还没有到n，必须再走下一步
    int jump(int A[], int n) {
        int curReach=0;
        int maxReach=0;
        int step=0;
        for(int i=0;i<n&&i<=maxReach;i++){
            if(i>curReach){ //step-1步能够到达的距离,必须再走一步了
                step++;
                curReach=maxReach;
            }
            maxReach=max(maxReach,i+A[i]); // step步最远距离
        }
        if(maxReach<n-1){
            return -1;
        }
        return step;
    }
};

```

# analysis
>分析见注释


# reference
[[编程题]jump-game-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/7250845fb3b946a5a778565adba9d993