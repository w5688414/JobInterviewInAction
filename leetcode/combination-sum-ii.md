# problem
>Given a collection of candidate numbers ( C ) and a target number ( T ), find all unique combinations in C where the candidate numbers sums to T .

Each number in C may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
Elements in a combination (a 1, a 2, … , a k) must be in non-descending order. (ie, a 1 ≤ a 2 ≤ … ≤ a k).
The solution set must not contain duplicate combinations.

For example, given candidate set10,1,2,7,6,1,5and target8, 
A solution set is: 
```
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]

```
# codes
```
class Solution {
public:
    vector<vector<int> > combinationSum2(vector<int> &num, int target) {
        vector<vector<int> > result;
        vector<int> ans;
        sort(num.begin(),num.end());
        int sum=0;
        combinationSum(sum,target,0,ans,num,result);
        return result;
    }
    
    void combinationSum(int sum,int target,int start,vector<int> ans,
                        vector<int> &num,vector<vector<int> > &result){
        if(sum==target){
            vector<vector<int> >::iterator iter;
            iter=find(result.begin(),result.end(),ans);
            if(iter==result.end()){
                result.push_back(ans);
            }
            
            return;
        }
        if(sum>target){
            return;
        }
        for(int i=start;i<num.size();i++){
            ans.push_back(num[i]);
            combinationSum(sum+num[i],target,i+1,ans,num,result);
            ans.pop_back();
        }
    }
};
```

# analysis
>唯一高兴的是，这是我自己写出来的，深度优先遍历再加上最后一步去重的操作。

# reference
[[编程题]combination-sum-ii][1]
[vector、map 判断某元素是否存在、查找指定元素][2]

[1]: https://www.nowcoder.com/questionTerminal/75e6cd5b85ab41c6a7c43359a74e869a
[2]: https://www.cnblogs.com/SZxiaochun/p/7131361.html