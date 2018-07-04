# problem
> Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:
```
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
```

Note:
Assume that the total area is never beyond the maximum possible value of int.

# codes
```
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int x1=max(A,E);
        int y1=max(B,F);
        int x2=min(C,G);
        int y2=min(D,H);
        if(A>=G||B>=H||E>=C||F>=D){
            return solve(A,B,C,D)+solve(E,F,G,H);
        }else{
            return solve(A,B,C,D)+solve(E,F,G,H)-solve(x1,y1,x2,y2);
        }   
    }
    int solve(int x1,int y1,int x2,int y2){
        return abs(x1-x2)*abs(y1-y2);
    }
};
```

# analysis
>这道题目虽然不难，主要的难点就是判断是否有交集，这个我并没有想出来，只需要比较一下几个边界就行了，看来我还是太年轻了。

# reference
[[LeetCode] Rectangle Area 矩形面积][1]

[1]: http://www.cnblogs.com/grandyang/p/4563153.html