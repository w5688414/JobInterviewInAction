# problem
>Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# codes
```
class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        int n=height.size();
        int result=0;
        stack<int> s;
        for(int i=0;i<height.size();i++){
            while(!s.empty()&&height[s.top()]>=height[i]){
                int h=height[s.top()];
                s.pop();
                result=max(result,(i-1-(s.empty()? (-1):s.top()))*h);
            }
            s.push(i);
        }
        while(!s.empty()){
            int h=height[s.top()];
            s.pop();
            result=max(result,(n-1-(s.empty()? (-1):s.top()))*h);           
        }
        return result;
    }
};

```

# analysis
- 用堆栈计算每一块板能延伸到的左右边界
- 对每一块板
- 堆栈顶矮，这一块左边界确定，入栈
- 堆栈顶高，堆栈顶右边界确定，出栈，计算面积
- 入栈时左边界确定
- 出栈时右边界确定
- 堆栈里元素是递增的
> 复杂度 O(n)


# reference
[[编程题]largest-rectangle-in-histogram][1]

[1]: https://www.nowcoder.com/questionTerminal/e3f491c56b7747539b93e5704b6eca40