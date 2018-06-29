# problem
>Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
```
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
```
Example 2:
```
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
```
Example 3:
```
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
```

# codes
```
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        vector<long> A(3,LONG_MIN);
        for(int i=0;i<nums.size();i++){
            if(A[0]<nums[i]){
                A[2]=A[1];
                A[1]=A[0];
                A[0]=nums[i];
                
            }else if(A[1]<nums[i]&&nums[i]<A[0]){
                A[2]=A[1];
                A[1]=nums[i];
            }else if(A[2]<nums[i]&&nums[i]<A[1]){
                A[2]=nums[i];
            }
        }
        
        return (A[2]==LONG_MIN||A[2]==A[1]) ? A[0]:A[2];
    }
};
```

# analysis
>那么我们三个变量A[0], A[1], A[2]来分别保存第一大，第二大，和第三大的数，然后我们遍历数组，如果遍历到的数字大于当前第一大的数A[0]，那么三个变量各自错位赋值，如果当前数字大于A[1]，小于A[0]，那么就更新A[1]和A[2]，如果当前数字大于A[2]，小于A[1]，那就只更新A[0]，注意这里有个坑，就是初始化要用长整型long的最小值，否则当数组中有INT_MIN存在时，程序就不知道该返回INT_MIN还是最大值first了，

# reference
[[LeetCode] Third Maximum Number 第三大的数][1]

[1]: http://www.cnblogs.com/grandyang/p/5983113.html

