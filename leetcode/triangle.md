# problem
>Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
The minimum path sum from top to bottom is11(i.e., 2 + 3 + 5 + 1 = 11).

Note: 
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

# codes
```
class Solution {
public:
    int minimumTotal(vector<vector<int> > &triangle) {
        vector<int> result(triangle.back());
        for(int i=triangle.size()-2;i>=0;i--){
            for(int j=0;j<triangle[i].size();j++){
                result[j]=triangle[i][j]+min(result[j],result[j+1]);
            }
        }
        return result[0];
    }
};

```

# analysis
>动态规划虽然难以理解，但是代码写起来超级简单，我们自底向上计算，先用最后一行的数组初始化我们的result容器，然后写出动态规划的式子
> result[j]=triangle[i][j]+min(result[j],result[j+1]);
> 它表示当前的最小路径，等于上一层最小路径的值加上当前路径的值。

# reference
[[编程题]triangle][1]


[1]: https://www.nowcoder.com/questionTerminal/2b7995aa4f7949d99674d975489cb7da
