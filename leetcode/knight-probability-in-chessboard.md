# problem
>On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:
```
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
```
Note:
1. N will be between 1 and 25.
2. K will be between 0 and 100.
3. The knight always initially starts on the board.

# codes
```
class Solution {
private:
vector<vector<int>> dirs{{-1,-2},{-2,-1},{-2,1},{-1,2},{1,2},{2,1},{2,-1},{1,-2}};
    
public:
    double knightProbability(int N, int K, int r, int c) {
        vector<vector<vector<double>>> memo(K+1,vector<vector<double>>(N,vector<double>(N,0.0)));
        return solve(memo,N,K,r,c)/pow(8, K);
    }
    
    double solve(vector<vector<vector<double>>>&memo,int N,int K,int r,int c){
        if(K==0){
            return 1.0;
        }
        if(memo[K][r][c]!=0.0){
            return memo[K][r][c];
        }
        for(auto dir:dirs){
            int x=r+dir[0];
            int y=c+dir[1];
            if(x<0||x>=N||y<0||y>=N){
                continue;
            }
            memo[K][r][c]+=solve(memo,N,K-1,x,y);
        }
        return memo[K][r][c];   
    }
};
```

# analysis
>记忆化数组的解法，dp的解法没有看懂，所以这个解法就先凑合一下喽。

# reference
[[LeetCode] Knight Probability in Chessboard 棋盘上骑士的可能性][1]


[1]: https://www.cnblogs.com/grandyang/p/7639153.html
