# problem
>Given a 2D board containing'X'and'O', capture all regions surrounded by'X'.

A region is captured by flipping all'O's into'X's in that surrounded region .

For example,
```
X X X X
X O O X
X X O X
X O X X
```
After running your function, the board should be:
```
X X X X
X X X X
X X X X
X O X X
```
# codes
```
class Solution {
private:
    queue<int> q;
public:
    void solve(vector<vector<char>> &board) {
        if(board.empty()||board.size()==0||board[0].size()==0){
            return ;
        }
        int m=board.size();
        int n=board[0].size();
        for(int i=0;i<n;i++){
            traverse(0,i,board,m,n);
            traverse(m-1,i,board,m,n);
        }
        for(int i=0;i<m;i++){
            traverse(i,0,board,m,n);
            traverse(i,n-1,board,m,n);
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(board[i][j]=='O'){
                    board[i][j]='X';
                }else if(board[i][j]=='Z'){
                    board[i][j]='O';
                }
            }
        }
    }
    void traverse(int x,int y,vector<vector<char>> &board,int m,int n){
        add(x,y,board,m,n);
        while(!q.empty()){
            int p=q.front();
            q.pop();
            int px=p/n;
            int py=p%n;
            add(px+1,py,board,m,n);
            add(px-1,py,board,m,n);
            add(px,py+1,board,m,n);
            add(px,py-1,board,m,n);
        }
    }
    void add(int x,int y,vector<vector<char>> &board,int m,int n){
        if(x>=0&&x<m&&y>=0&&y<n&&board[x][y]=='O'){
            board[x][y]='Z';
            q.push(x*n+y);
        }
    }
};

```

# analysis
>遍历矩阵的四条边，如果出现O字符，我们把O替换为Z，然后沿着这个点深度优先遍历找与之相邻的O，同样置为Z，最后我们把Z的用O替换，把原来的O用X替换
# reference
[Leetcode---Surrounded Regions][1]
[[编程题]surrounded-regions][2]

[1]: http://blog.chinaunix.net/uid-29822702-id-4490740.html
[2]: https://www.nowcoder.com/questionTerminal/c159db5028034aa595043a1a220a62dd

