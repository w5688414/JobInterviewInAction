# problem
>Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

1. If a mine ('M') is revealed, then the game is over - change it to 'X'.
2. If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
4. Return the board when no more squares will be revealed.
Example 1:
```
Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

```
Example 2:
```
Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
```

# codes

```
class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        if(board.empty()) return {};
        int m=board.size();
        int n=board[0].size();
        int row=click[0];
        int col=click[1];
        int cnt=0;
        if(board[row][col]=='M'){
            board[row][col]='X';
        }else{
            for(int i=-1;i<2;i++){
                for(int j=-1;j<2;j++){
                    int x=i+row; int y=col+j;
                    if(x<0||x>=m||y<0||y>=n) continue;
                    if(board[x][y]=='M'){
                        cnt++;
                    }
                }
            }
            if(cnt>0){
                board[row][col]=cnt+'0';
            }else{
                board[row][col]='B';
                for(int i=-1;i<2;i++){
                    for(int j=-1;j<2;j++){
                        int x=i+row; int y=col+j;
                        if(x<0||x>=m||y<0||y>=n) continue;
                        if(board[x][y]=='E'){
                            vector<int> nextPos{x,y};
                            updateBoard(board,nextPos);
                        }
                    }
                }
            }
        }
        return board;
    }
};
```

# analysis
>这是一个扫雷游戏，虽然没做出来，但是我觉得蛮有意思的，感觉仔细看题了之后，也能做出来的。

# reference
[[LeetCode] Minesweeper 扫雷游戏][1]
[1]: http://www.cnblogs.com/grandyang/p/6536694.html