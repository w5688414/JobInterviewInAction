# problem
>Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character'.'.

# codes
```
class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        if(board.empty()){
            return false;
        }
        return solve(board);
    }
    bool solve(vector<vector<char> > &board){
        int n=board.size();
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(board[i][j]!='.'){
                    if(!isValid(board,i,j)){
                        return false;
                    }
                }
            }
        }
        return true;
    }
    bool isValid(vector<vector<char> > board,int row,int col){
        int n=board.size();
        for(int i=0;i<n;i++){
            // 行
            if(board[row][col]==board[row][i]&&col!=i){ 
                return false;
            }
            //列
            if(board[row][col]==board[i][col]&&i!=row){
                return false;
            }
        }
        //九宫格
        for(int i=row/3*3;i<row/3*3+3;i++){
            for(int j=col/3*3;j<col/3*3+3;j++){
                if(board[row][col]==board[i][j]&&(i!=row||j!=col)){
                    return false;
                }
            }
        }
        return true;
    }
};
```

# analysis
>这是一个经典的问题，我也做不出来，大概是功力不够的缘故吧，努力加油。 one time you will be good enough.每遍历到一个数字，我们需要验证该数字在其对应的行是否合法，列是否合法，在小九宫格里面是否合法。

# reference
[[编程题]valid-sudoku][1]


[1]: https://www.nowcoder.com/questionTerminal/8240bcdab4eb496fb6c4ba634fc67921
