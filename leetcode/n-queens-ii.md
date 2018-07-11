# problem
>The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
Example:
```
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```

# codes
```
class Solution {
private:
    int x[19];
public:
    int totalNQueens(int n) {
        int res=0;
        solve(0,n,res);
        return res;
    }
    void solve(int start,int n,int& res){
        if(start==n){
            res++;
            return;
        }
        for(int i=0;i<n;i++){
            x[start]=i;
            if(check(start)){
                solve(start+1,n,res);
            }
        }
    }
    bool check(int m){
        for(int i=0;i<m;i++){
            if(abs(x[m]-x[i])==abs(m-i)||x[m]==x[i]){
                return false;
            }
        }
        return true;
    }
};
```

# analysis
>8皇后问题，这是第四次做了，感觉还是不怎么适应，不过现在已经能够很好的理解了，希望后面能够自己独立的写出来。

# reference
[52. N-Queens II][1]

[1]: https://leetcode.com/problems/n-queens-ii/description/