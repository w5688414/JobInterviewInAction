# problem
>An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.

What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return -1.

```
Examples:
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation:
One potential sequence of moves is shown below, from left to right:

0110     1010     1010
0110 --> 1010 --> 0101
1001     0101     1010
1001     0101     0101

The first move swaps the first and second column.
The second move swaps the second and third row.


Input: board = [[0, 1], [1, 0]]
Output: 0
Explanation:
Also note that the board with 0 in the top left corner,
01
10

is also a valid chessboard.

Input: board = [[1, 0], [1, 0]]
Output: -1
Explanation:
No matter what sequence of moves you make, you cannot end with a valid chessboard.
```
Note:

- board will have the same number of rows and columns, a number in the range [2, 30].
- board[i][j] will be only 0s or 1s.


# codes
```
class Solution {
public:
    int movesToChessboard(vector<vector<int>>& board) {
        int n=board.size(),rowSum=0,colSum=0,rowSwap=0,colSwap=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(board[0][0]^board[i][0]^board[0][j]^board[i][j]){
                    return -1;
                }
            }
        }
        for(int i=0;i<n;i++){
            rowSum+=board[i][0];
            colSum+=board[0][i];
            rowSwap+=board[i][0]==i%2;
            colSwap+=board[0][i]==i%2;
        }
        if(n/2>rowSum||rowSum>(n+1)/2) return -1;
        if(n/2>colSum||colSum>(n+1)/2) return -1;
        if(n%2){
            if (colSwap % 2) colSwap = n - colSwap;
            if (rowSwap % 2) rowSwap = n - rowSwap;
        }else{
            colSwap=min(n-colSwap,colSwap);
            rowSwap = min(n - rowSwap, rowSwap);
        }
        return (colSwap+rowSwap)/2;
    }
};
```

# analysis
>这道题完全一脸懵
Two conditions to help solve this problem:

- In a valid chess board, there are 2 and only 2 kinds of rows and one is inverse to the other.
For example if there is a row 01010011 in the board, any other row must be either 01010011 or 10101100.
The same for columns
A corollary is that, any rectangle inside the board with corners top left, top right, bottom left, bottom right must be 4 zeros or 2 ones 2 zeros or 4 zeros.

- Another important property is that every row and column has half ones. Assume the board is N * N:
If N = 2*K, every row and every column has K ones and K zeros.
If N = 2*K + 1, every row and every column has K ones and K + 1 zeros or K + 1 ones and K zeros.


# reference
[782. Transform to Chessboard][1]

[1]: https://leetcode.com/problems/transform-to-chessboard/discuss/114847/Easy-and-Concise-Solution-with-Explanation-C++JavaPython


