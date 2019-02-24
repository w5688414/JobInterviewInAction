# problem
>Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# codes

## solution 1
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
## solution 2
```
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(-1);
        stack<int> s;
        int index=0;
        int sum=0;
        while(index<heights.size()){
            if(s.size()==0||heights[s.top()]<=heights[index]){
                s.push(index);
                index++;
            }else{
                int base=s.top();
                s.pop();
                int max_area=0;
                if(s.size()==0){
                    max_area=heights[base]*index;
                }else{
                    max_area=heights[base]*(index-1-s.top());
                }
                if(sum<max_area){
                    sum=max_area;
                }
            }
        }
        return sum;
    }
};
```
> 如果第一个版本看不懂，可以看看第二个版本，思路应该比较清晰，栈存储的是下标，维护的是递增序列，如果不递增，则出栈计算长度。

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
[leetcode之Largest Rectangle in Histogram][2]

[1]: https://www.nowcoder.com/questionTerminal/e3f491c56b7747539b93e5704b6eca40
[2]: https://blog.csdn.net/yutianzuijin/article/details/52072427
