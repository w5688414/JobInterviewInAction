# problem
> A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:
```
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
```
Example 2:
```
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
```
Notes:
1. Both rectangles rec1 and rec2 are lists of 4 integers.
2. All coordinates in rectangles will be between -10^9 and 10^9.

# codes
```
class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        return !(rec1[2]<=rec2[0]||rec1[3]<=rec2[1]||rec1[0]>=rec2[2]||rec1[1]>=rec2[3]);
    }
};
```

# analysis
>反过来，如果能列举他们不重叠的情况，就能得到他们重叠的情况了，思想很简单，我还是没有想到。

# reference
[836. Rectangle Overlap][1]

[1]: https://leetcode.com/problems/rectangle-overlap/solution/