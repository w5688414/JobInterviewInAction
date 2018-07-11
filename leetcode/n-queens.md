# problem
>The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where'Q'and'.'both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
```
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
    int x[19];
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> out;
        string s1(n,'.');
        for(int i=0;i<n;i++){
            out.push_back(s1);
        }
        solve(res,out,0,n);
        return res;
    }
    void solve(vector<vector<string>>& res,vector<string> out,int start,int n){
        if(start==n){
            res.push_back(out);
            return ;
        }
        for(int i=0;i<n;i++){
            x[start]=i;
            out[start][i]='Q';
            if(check(start)){
                solve(res,out,start+1,n);
            }
            out[start][i]='.';
        }
    }
    bool check(int m){
        for(int i=0;i<m;i++){
            if(abs(x[m]-x[i])==abs(m-i)||x[m]==x[i]) return false;
        }
        return true;
    }
};

```

# analysis
>8皇后问题，我已经做了三次了，但是总感觉不那么顺手，看来后面还需要加强。使用的是回溯法，注意x的妙用，x[start]=j，表示第start行第j列的值为皇后。

# reference
[[编程题]n-queens][1]

[1]: https://www.nowcoder.com/questionTerminal/c77ac599d0764433a5946610a7626768