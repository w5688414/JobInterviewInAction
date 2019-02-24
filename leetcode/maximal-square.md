# problem
>Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# codes
```
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int res=0;
        for(int i=0;i<matrix.size();i++){
            vector<int> v(matrix[i].size(),0);
            for(int j=i;j<matrix.size();j++){
                for(int k=0;k<matrix[j].size();k++){
                    if(matrix[j][k]=='1') v[k]++;
                }
                res=max(res,getSquareArea(v,j-i+1));
            }
        }
        return res;
    }
    int getSquareArea(vector<int> &v,int k){
        if(v.size()<k){
            return 0;
        }
        int count=0;
        for(int i=0;i<v.size();i++){
            if(v[i]!=k) count=0;
            else{
                count++;
            }
            if(count==k){
                return k*k;
            }
        }
        return 0;
    }
};
```

# analysis
>说实话，我还真不大懂这一题，留着慢慢看吧。今后找个机会把这些东西全都整理下来。

```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
step 1
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0    v=1,0,1,0,0
```

step 2
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0    v=2,0,2,1,1
```

step 3
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0    v=3,1,3,2,2
```
step 4
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0    v=4,1,3,3,2
```

# reference
[[LeetCode] Maximal Square 最大正方形][1]


[1]: https://www.cnblogs.com/grandyang/p/4550604.html
