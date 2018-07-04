# problem
>You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.
Example 1:
```
Given x = [2, 1, 1, 2],
?????
?   ?
???????>
    ?

Return true (self crossing)
```
Example 2:
```
Given x = [1, 2, 3, 4],
????????
?      ?
?
?
?????????????>

Return false (not self crossing)
```
Example 3:
```
Given x = [1, 1, 1, 1],
?????
?   ?
?????>

Return true (self crossing)
```

# codes
```
class Solution {
public:
    bool isSelfCrossing(vector<int>& x) {
        for(int i=3;i<x.size();i++){
            if(x[i]>=x[i-2]&&x[i-3]>=x[i-1]){
                return true;
            }
            if(i>=4&&x[i-1]==x[i-3]&&x[i]+x[i-4]>=x[i-2]){
                return true;
            }
            if(i>=5&&x[i-2]>=x[i-4]&&x[i-3]>=x[i-1]&&x[i-1]+x[i-5]>=x[i-3]&&x[i]+x[i-4]>=x[i-2]){
                return true;
            }
        }
        return false;
    }
};
```

# analysis
>相交只有以下三种情况：
```
     x(1)
    ┌───┐
x(2)│   │x(0)
    └───┼──>
    x(3)│
        
```
第一类是第四条边和第一条边相交的情况，需要满足的条件是第一条边大于等于第三条边，第四条边大于等于第二条边。同样适用于第五条边和第二条边相交，第六条边和第三条边相交等等，依次向后类推的情况...

```
      x(1)
    ┌──────┐
    │      │x(0)
x(2)│      ^
    │      │x(4)
    └──────│
      x(3)
```
第二类是第五条边和第一条边重合相交的情况，需要满足的条件是第二条边和第四条边相等，第五条边大于等于第三条边和第一条边的差值，同样适用于第六条边和第二条边重合相交的情况等等依次向后类推...

```
      x(1)
    ┌──────┐
    │      │x(0)
x(2)│     <│────│
    │       x(5)│x(4)
    └───────────│
        x(3)
```
第三类是第六条边和第一条边相交的情况，需要满足的条件是第四条边大于等于第二条边，第三条边大于等于第五条边，第五条边大于等于第三条边和第一条边的差值，第六条边大于等于第四条边和第二条边的差值，同样适用于第七条边和第二条边相交的情况等等依次向后类推...

这道题我是真不会，也挺服气，毕竟我觉得不看答案完全做不出来。

# reference
[[LeetCode] Self Crossing 自交][1]

[1]: http://www.cnblogs.com/grandyang/p/5216856.html

