# problem
>Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:
```
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

# codes
```
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        if(numRows==0){
            return res;
        }
        vector<int> ans(numRows,0);
        ans[0]=1;
        for(int i=0;i<numRows;i++){
            for(int j=i;j>0;j--){
                ans[j]=ans[j]+ans[j-1];
            }
            vector<int> temp;
            for(int k=0;k<=i;k++){
                temp.push_back(ans[k]);
            }
            res.push_back(temp);
        }
        return res;
    }
};
```

# analysis
>这道题目我后面发现可以自己做出来了，所以去做了一下。发现并不是想象的难。

# reference
[[编程题]pascals-triangle-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/a60ee4a1c8a04c3a93f1de3cf9c16f19