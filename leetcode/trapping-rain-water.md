# problem
>Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given[0,1,0,2,1,0,1,3,2,1,2,1], return6.


# codes
```
class Solution {
public:
    int trap(vector<int>& height) {
        int i=0;
        int j=height.size()-1;
        int sum=0;
        int left_max=0;
        int right_max=0;
        while(i<j){
            left_max=max(left_max,height[i]);
            right_max=max(right_max,height[j]);
            if(left_max<right_max){
                sum+=(left_max-height[i]);
                i++;
            }else{
                sum+=(right_max-height[j]);
                j--;
            }
        }
        return sum;
    }
};
```

# analysis

题目的意思是：给你一个柱形图，然后往里面注水，问柱形图能够装得下多大面积的水。

- 索引i从左到右，索引j从右往左，遍历的时候寻找左右两边的最大值，如果左边的最大值小于右边的最大值，左边进行操作；如果左边的最大值大于等于右边的最大值，右边进行操作。直到i>j时终止。
# reference
[42. Trapping Rain Water][1]

[1]: https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution.


