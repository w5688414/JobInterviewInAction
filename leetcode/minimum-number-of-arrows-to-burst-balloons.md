# problem
>There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:
```
Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
```
# codes
```
class Solution {
public:
    int findMinArrowShots(vector<pair<int, int>>& points) {
        if(points.empty()) return 0;
        sort(points.begin(),points.end());
        int res=1;
        int end=points[0].second;
        for(int i=1;i<points.size();i++){
            if(points[i].first<=end){
                end=min(end,points[i].second);
            }else{
                res++;
                end=points[i].second;
            }
        }
        return res;
    }
};
```

# analysis
>我们一堆大小不等的气球，用区间范围来表示气球的大小，可能会有重叠区间。然后我们用最少的箭数来将所有的气球打爆。
这道题是典型的用贪婪算法来做的题，因为局部最优解就等于全局最优解.

把重叠区域都合并，然后计算个数就是结果了。

# reference
[[LeetCode] Minimum Number of Arrows to Burst Balloons 最少数量的箭引爆气球][1]

[1]: http://www.cnblogs.com/grandyang/p/6050562.html