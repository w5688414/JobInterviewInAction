# problem
>Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

# codes
```
class Solution {
public:
    int maximalRectangle(vector<vector<char> > &matrix) {
        if(matrix.size()==0){
            return 0;
        }
        int rows=matrix.size();
        int cols=matrix[0].size();
        int sum=0;
        vector<int >temp(cols,0);
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                temp[j]=matrix[i][j]-'0'+(matrix[i][j]-'0')*temp[j];
            }
            sum=max(largestRectangleArea(temp),sum);
        }
        return sum;
    }
    int largestRectangleArea(vector<int> &height){
        int max_area=0;
        for(int i=0;i<height.size();i++){
            int MIN=height[i];
            for(int j=i;j<height.size();j++){
                MIN=min(height[j],MIN);
                int CurArea=MIN*(j-i+1);
                if(max_area<CurArea){
                    max_area=CurArea;
                }
            }
        }
        return max_area;
    }
};
```

# analysis
>说实话，我还真不大懂这一题，留着慢慢看吧。今后找个机会把这些东西全都整理下来。

# reference
[[编程题]maximal-rectangle][1]
[1]: https://www.nowcoder.com/questionTerminal/b65c0f05e1dc4588b91c615fa7c7ef78