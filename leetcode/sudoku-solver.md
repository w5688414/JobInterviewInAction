# problem
>Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character'.'.

You may assume that there will be only one unique solution.

# codes
```
class Solution {
public:
    void solveSudoku(vector<vector<char> > &board) {
        if(board.empty()){
            return;
        }
        solve(board);
    }
    bool solve(vector<vector<char> > &board){
        int n=board.size();
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(board[i][j]=='.'){
                    for(char c='1';c<='9';c++){
                        if(isValid(board,i,j,c)){
                            board[i][j]=c;
                            if(solve(board)){
                                return true;
                            }else{
                                board[i][j]='.';
                            }
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    bool isValid(vector<vector<char> > board,int row,int col,char num){
        int n=board.size();
        for(int i=0;i<n;i++){
            // 判断col列和row行是否满足数独条件
            if(board[i][col]==num||board[row][i]==num){
                return false;
            }
            // 判断九宫格
            if(board[3*(row/3)+i/3][3*(col/3)+i%3]==num){
                return false;
            }
        }
        return true;
    }
};
```

# analysis
>这是一个跟八皇后很相似的一个问题，可惜我也写不出来，看来还需要不断的练习。

# reference
[[编程题]sudoku-solver][1]

[1]: https://www.nowcoder.com/questionTerminal/5e6c424b82224b85b64f28fd85761280
