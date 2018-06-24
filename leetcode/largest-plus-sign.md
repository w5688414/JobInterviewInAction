# problem
>In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

```
Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
```
Example 1:
```
Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
```

Example 2:
```
Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
```

Example 3:
```
Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.
```

Note:
1. N will be an integer in the range [1, 500].
2. mines will have length at most 5000.
3. mines[i] will be length 2 and consist of integers in the range [0, N-1].

# codes
```
class Solution {
public:
    int orderOfLargestPlusSign(int N, vector<vector<int>>& mines) {
        int res=0;
        int cnt=0;
        vector<vector<int>> dp(N,vector<int>(N,0));
        unordered_set<int> s;
        for(auto mine:mines){
            s.insert(mine[0]*N+mine[1]);
        }
        for(int j=0;j<N;j++){
            cnt=0;
            for(int i=0;i<N;i++){ //up
                cnt=s.count(i*N+j) ? 0:cnt+1;
                dp[i][j]=cnt;
            }
            cnt=0;
            for(int i=N-1;i>=0;i--){  //down
                cnt=s.count(i*N+j) ? 0:cnt+1;
                dp[i][j]=min(dp[i][j],cnt);
            }
        }
        
        for(int i=0;i<N;i++){
            cnt=0;
            for(int j=0;j<N;j++){ //left
                cnt=s.count(i*N+j) ? 0:cnt+1;
                dp[i][j]=min(dp[i][j],cnt);
            }
            cnt=0;
            for(int j=N-1;j>=0;j--){  //right
                cnt=s.count(i*N+j) ? 0:cnt+1;
                dp[i][j]=min(dp[i][j],cnt);
                res=max(dp[i][j],res);
            }
        }
        return res;
    }
    
};
```

# analysis
>这道题的暴力破解我试了一下是超时，dp的解法，我觉得一般人想不到。
暴力搜索的时间复杂度之所以高的原因是因为对于每一个1都要遍历其上下左右四个方向，有大量的重复计算，我们为了提高效率，可以对于每一个点，都计算好其上下左右连续1的个数。博主最先用的方法是建立四个方向的dp数组，dp[i][j]表示 (i, j) 位置上该特定方向连续1的个数，那么就需要4个二维dp数组，例如：

原数组：
```
1  0  1  0
1  1  1  1
1  0  1  1
```
那么我们建立left数组是当前及其左边连续1的个数，如下所示：
```
1  0  1  0
1  2  3  4
1  0  1  2
```
right数组是当前及其右边连续1的个数，如下所示：
```
1  0  1  0
4  3  2  1
1  0  2  1
```
up数组是当前及其上边连续1的个数，如下所示：
```
1  0  1  0
2  1  2  1
3  0  3  2
```
down数组是当前及其下边连续1的个数，如下所示：
```
3  0  3  0
2  1  2  2
1  0  1  1
```
我们需要做的是在这四个dp数组中的相同位置的四个值中取最小的一个，然后在所有的这些去除的最小值中选最大一个返回即可。为了节省空间，我们不用四个二维dp数组，而只用一个就可以了，因为对于每一个特定位置，我们只需要保留较小值，所以在更新的时候，只需要跟原来值相比取较小值即可。在计算down数组的时候，我们就可以直接更新结果res了，因为四个值都已经计算过了，我们就不用再重新在外面开for循环了.


# reference
[[LeetCode] Largest Plus Sign 最大的加型符号][1]

[1]: http://www.cnblogs.com/grandyang/p/8679286.html