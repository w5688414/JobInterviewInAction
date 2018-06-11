# problem
>You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

# codes
```
class Solution {
public:
//做两次翻转，先沿右上-左下的对角线翻转，再沿水平中线上下翻转
    void rotate(vector<vector<int> > &matrix) {
        int rows=matrix.size();
        int cols=matrix[0].size();
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols-i;j++){
                swap(matrix[i][j],matrix[rows-j-1][cols-i-1]);
            }
        }
        for(int i=0;i<rows/2;i++){
            for(int j=0;j<cols;j++){
                swap(matrix[i][j],matrix[rows-i-1][j]);
            }
        }
        
    }
};
```

# analysis
>[[1,2],[3,4]]->[[4,2],[3,1]]->[[3,1],[4,2]]
我发现leetcode的解法还是蛮多的，不过大体跟我的类似，我把参考贴出来了，供大家参考一下。
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/

/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/

## reference
[[编程题]rotate-image][1]
[48. Rotate Image][2]

[1]: https://www.nowcoder.com/questionTerminal/4018c0c6d15d473e804656afcbc2c501
[2]: https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image