# problem
>A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

- Players take turns placing characters into empty squares (" ").
- The first player always places "X" characters, while the second player always places "O" characters.
- "X" and "O" characters are always placed into empty squares, never filled ones.
- The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
- The game also ends if all squares are non-empty.
- No more moves can be played if the game is over.

```
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
```
Note:

- board is a length-3 array of strings, where each string board[i] has length 3.
- Each board[i][j] is a character in the set {" ", "X", "O"}.

# codes
```
class Solution {
public:
    bool validTicTacToe(vector<string>& board) {
        int cx=cnt(board,'X'), co=cnt(board,'O');
        bool wx=win(board,'X'), wo=win(board,'O');
        if(wx&&wo) return false;
        if(wx) return cx==co+1;
        if(wo) return cx==co;
        return cx==co+1||co==cx;
    }
    int cnt(vector<string> b,char c){
        int res=0;
        for(string s:b){
            res+=count(s.begin(),s.end(),c);
        }
        return res;
    }
    bool win(vector<string> b, char c){
        for(int i=0;i<3;i++){
            if(b[i][0]==c&&b[i][1]==c&&b[i][2]==c){
                return true;
            }
        }
        for(int j=0;j<3;j++){
            if(b[0][j]==c&&b[1][j]==c&&b[2][j]==c){
                return true;
            }
        }
        return (b[0][0]==c&&b[1][1]==c&&b[2][2]==c)||(b[0][2]==c&&b[1][1]==c&&b[2][0]==c);
    }
};
```

# analysis
>大概是脑子短路了，连题目的意思都没弄懂。

1. 由规则可知，”X”一定最先开始，所以当前局面存在”O”的个数大于”X”的个数为非法。 
2. 其次，由于”X”和”O”轮流，因此，当前局面中”X”的个数要么和”O”相等，要么比”O”多一。 
3. “O”在当前局面赢得比赛的情况下，上一轮的”X”一定不能赢得局面。 
4. “O”在当前局面赢得比赛的情况下，上一轮的”X”没有赢得局面时，合法局面必须满足”O”的个数等于”X”的个数。 
5. “X”在当前局面赢得比赛的情况下，意味着上一轮”O”没有赢得局面，合法局面下，”X”的个数正好比”O”的个数多一。

# reference
[794. Valid Tic-Tac-Toe State][1]
[LWC 74: 794. Valid Tic-Tac-Toe State][2]


[1]: https://leetcode.com/problems/valid-tic-tac-toe-state/discuss/117603/Concise-C++-solution-(-EASY-to-understand-)-with-explanation
[2]: https://blog.csdn.net/u014688145/article/details/79451723