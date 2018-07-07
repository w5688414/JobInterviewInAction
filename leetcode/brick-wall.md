# problem
>There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
Example:
```
Input: 
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
Output: 2
```
Note:
1. The width sum of bricks in different rows are the same and won't exceed INT_MAX.
2. The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.

# codes
```
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        int mx=0;
        unordered_map<int,int> m;
        for(auto a:wall){
            int sum=0;
            for(int i=0;i<a.size()-1;i++){
                sum+=a[i];
                m[sum]++;
                mx=max(mx,m[sum]);
            }
        }
        return wall.size()-mx;
    }
};
```

# analysis
>我们用hash表建立断点与频率的映射，所以我们只要找到出现断点频率最多的地方断开就能损坏最小的砖。我知道要这么做，但是我没想到怎么建模，看来我还需要继续改进。

# reference
[[LeetCode] Brick Wall 砖头墙壁][1]


[1]: http://www.cnblogs.com/grandyang/p/6697067.html