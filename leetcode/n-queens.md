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
private:
    int x[9];
    vector<vector<string> > result;
public:
    vector<vector<string> > solveNQueens(int n) {
        string s1(n,'.');
        vector<string> res;
        for(int i=0;i<n;i++){
            res.push_back(s1);
        }
        backTrack(0,n,res);
        return result;
    }
    void backTrack(int start,int n,vector<string> res){
        if(start==n){
            result.push_back(res);
            return ;
        }else{
            for(int i=0;i<n;i++){
                x[start]=i;
                if(check(start)){
                   res[start][i]='Q';
                   backTrack(start+1,n,res);
                   res[start][i]='.';
                }
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
>8皇后问题，我已经做了三次了，但是总感觉不那么顺手，看来后面还需要加强。使用的是回溯法，注意x的妙用，x[start]=j，表示第start行第j列的值为皇后。

# reference
[[编程题]n-queens][1]

[1]: https://www.nowcoder.com/questionTerminal/c77ac599d0764433a5946610a7626768