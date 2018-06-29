# problem
>Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
```
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
```
Note:
1. The length of the given array won't exceed 1000.
2. The integers in the given array are in the range of [0, 1000].

# codes
```
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        
        sort(nums.begin(),nums.end());
        int sum=0;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                int target=nums[i]+nums[j];
                int k=j+1;
                while(k<nums.size()&&target>nums[k]){
                    k++;
                }
                sum+=k-j-1;
            }
        }
        return sum;
    }
};
```

# analysis
>这道题用两边之和大于第三边的方法的话，就很暴力了，我们换一下，给数组排一下顺序，如果两个小边>大边就行了。然后就变成了3 sum的暴力问题了。哈哈哈哈，我还是没做出来。

# reference
[611. Valid Triangle Number][1]


[1]: https://leetcode.com/problems/valid-triangle-number/solution/