# problem
>Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```
# codes
```
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> result;
        for(int i=0;i<nums.size();i++){
            int idx=abs(nums[i])-1;
            if(nums[idx]>0){
                nums[idx]=-nums[idx];
            }
        }
        for(int i=0;i<nums.size();i++){
            if(nums[i]>0){
                result.push_back(i+1);
            }
        }
        return result;
    }
};
```

# analysis
>对于每个数字nums[i]，如果其对应的nums[nums[i] - 1]是正数，我们就赋值为其相反数，如果已经是负数了，就不变了，那么最后我们只要把留下的整数对应的位置加入结果res中即可.

# reference
[[LeetCode] Find All Numbers Disappeared in an Array 找出数组中所有消失的数字][1]

[1]: https://www.cnblogs.com/grandyang/p/6222149.html