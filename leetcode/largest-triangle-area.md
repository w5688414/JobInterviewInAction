# problem
>You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.
```
Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.
```
Notes:

- 3 <= points.length <= 50.
- No points will be duplicated.
- -50 <= points[i][j] <= 50.
- Answers within 10^-6 of the true value will be accepted as correct.


# codes

```
class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        double res=0;
        for(auto i:points){
            for(auto j:points){
                for(auto k:points){
                    res=max(res,solve(i,j,k));
                }
            }
        }
        return res;
    }
    double solve(vector<int>i,vector<int> j,vector<int> k){
        return 0.5*abs(i[0]*j[1]+j[0]*k[1]+k[0]*i[1]-j[0]*i[1]-k[0]*j[1]-i[0]*k[1]);
    }
};
```

# analysis
- 根据坐标求三角形的面积，公式我并没有推导过，并不会，不过我觉得简单，我以为有什么精妙的算法，原来是暴力破解。
S=0.5*A*B*sin(C)
推导而来。

# reference
[812. Largest Triangle Area][1]


[1]: https://leetcode.com/problems/largest-triangle-area/discuss/122711/C++JavaPython-Solution-with-Explanation-and-Prove