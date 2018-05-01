# problem
>Given n non-negative integers a1 , a2 , ..., an , where each represents a point at coordinate (i, ai ). n vertical lines are drawn such that the two endpoints of line i is at (i, ai ) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

# codes
```
class Solution {
public:
    int maxArea(vector<int> &height) {
        int low=0;
        int high=height.size()-1;
        int max_area=-1;
        while(low<high){
            int min_height=min(height[low],height[high]);
            int len=high-low;
            max_area=max(max_area,min_height*len);
            if(height[low]<height[high]){
                low++;
            }else{
                high--;
            }
        }
        return max_area;
    }
};
```

# analysis
>开始想到了栈，发现错了，看了别人的答案，发现这么简单。
- 一是两边往中间找，二是每次放弃最短的版。
这么做的原因在于：从起点和终点开始找，宽度最大，这时每移动一次其中一个点，必然宽度变小。
如此一来，想求最大，只有高度增长才有可能做到，去掉限制----短板，即放弃高度较小的点。

# reference
[[编程题]container-with-most-water][1]

[1]: https://www.nowcoder.com/questionTerminal/c97c1400a425438fb130f54fdcef0c57