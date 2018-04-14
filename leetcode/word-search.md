# problem
>Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =
```
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
```
word ="ABCCED", -> returnstrue,
word ="SEE", -> returnstrue,
word ="ABCB", -> returnsfalse.

# codes
```
class Solution {
public:
    bool exist(vector<vector<char> > &board, string word) {
        int rows=board.size();
        int cols=board[0].size();
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
               if(board[i][j]==word[0]){
                   if(DFS(board,word,0,i,j)){
                       return true;
                   }
               }
            }
        }
        return false;
    }
    
    bool isOut(int row, int col,int rows,int cols){
        return row<0|| row>=rows||col<0||col>=cols;
    }
    bool DFS(vector<vector<char> > &board,string word, int start,int row,int col){
      if(start>=word.size()){
          return true;
      }
          
      if(isOut(row,col,board.size(),board[0].size())){
          return false;
      }
      if(board[row][col]!=word[start]){
          return false;
      }
      int dx[]={0, 0, 1, -1};
      int dy[]={1, -1, 0, 0};
      char temp=board[row][col];
      board[row][col]='.';
      for(int i=0;i<4;i++){
          if(DFS(board,word,start+1,row+dx[i],col+dy[i])){
              return true;
          }
      }
      board[row][col]=temp;
      return false;
    }
};

```

# analysis
>深度优先搜索，本人不怎么会，然后这道题目没有做出来，看来后面需要继续加强。

# reference
[[编程题]word-search][1]

[1]: https://www.nowcoder.com/questionTerminal/14bcbcb7ae3c40c9bdbc5a0861361c29