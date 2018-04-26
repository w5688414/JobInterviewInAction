# problem
>Given a set of candidate numbers ( C ) and a target number ( T ), find all unique combinations in C where the candidate numbers sums to T .

The same repeated number may be chosen from C unlimited number of times.

Note:

All numbers (including target) will be positive integers.
Elements in a combination (a 1, a 2, … , a k) must be in non-descending order. (ie, a 1 ≤ a 2 ≤ … ≤ a k).
The solution set must not contain duplicate combinations.

For example, given candidate set2,3,6,7and target7, 
A solution set is: 
```
[7]
[2, 2, 3]
```
# codes
```
class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        vector<vector<int> > result;
        vector<int> ans;
        sort(candidates.begin(),candidates.end());
        combinationSum(result,ans,candidates,target,0,0);
        return result;
    }
    
    void combinationSum(vector<vector<int> > &result,vector<int> ans,
                        vector<int> &candidates,int target, int start,int sum){
        if(sum>target){
            return;
        }
        if(sum==target){
            result.push_back(ans);
            return ;
        }
        for(int i=start;i<candidates.size();i++){
            ans.push_back(candidates[i]);
            combinationSum(result,ans,candidates,target,i,sum+candidates[i]);
            ans.pop_back();
        }
        
    }
};
```

# analysis
>我开始还在对每个元素的使用无限制困扰呢，后面发现只需要小小的改变就行了，看来我还没有达到灵活运用的能力，还需要努力。

# reference
[[编程题]combination-sum][1]

[1]: https://www.nowcoder.com/questionTerminal/ff509107d96148778f6a14c885d74ace
