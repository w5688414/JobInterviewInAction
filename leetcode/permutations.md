# problem
>Given a collection of distinct integers, return all possible permutations.
Example:
```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

# codes

```
class Solution {
private:
    vector<vector<int>> result;
public:
    vector<vector<int>> permute(vector<int>& nums) {
        DFS(nums,0);
        return result;
    }
    void DFS(vector<int>& nums,int index){
        if(index==nums.size()){
            result.push_back(nums);
        }
        for(int i=index;i<nums.size();i++){
            swap(nums[index],nums[i]);
            DFS(nums,index+1);
            swap(nums[index],nums[i]);
        }
    }
};
```
# analysis
>这种解法我并没有想出来，仅仅用了交换和递归就行了，我一开始想到了visit数组来记录，发现这种方式更好，不需要额外的空间。

## reference
[46. Permutations][1]

[1]: https://leetcode.com/problems/permutations/discuss/137571/Small-C++-code-using-swap-and-recursion
