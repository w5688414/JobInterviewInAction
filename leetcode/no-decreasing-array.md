# problem
>Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
```
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
```
Example 2:
```
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
```
Note: The n belongs to [1, 10,000].


# codes

## s1
```
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int cnt=1;
        for(int i=1;i<nums.size();i++){
            if(nums[i]<nums[i-1]){
                if(cnt==0){
                    return false;
                }
                if(i==1||nums[i]>=nums[i-2]){
                    nums[i-1]=nums[i];
                }else{
                    nums[i]=nums[i-1];
                }
                cnt--;
            }
        }
        return true;
    }
};

```

# analysis

4，2，3

-1，4，2，3

2，3，3，2，4

我们通过分析上面三个例子可以发现，当我们发现后面的数字小于前面的数字产生冲突后，有时候需要修改前面较大的数字(比如前两个例子需要修改4)，有时候却要修改后面较小的那个数字(比如前第三个例子需要修改2)，那么有什么内在规律吗？是有的，判断修改那个数字其实跟再前面一个数的大小有关系，首先如果再前面的数不存在，比如例子1，4前面没有数字了，我们直接修改前面的数字为当前的数字2即可。而当再前面的数字存在，并且小于当前数时，比如例子2，-1小于2，我们还是需要修改前面的数字4为当前数字2；如果再前面的数大于当前数，比如例子3，3大于2，我们需要修改当前数2为前面的数3。这是修改的情况，由于我们只有一次修改的机会，所以用一个变量cnt，初始化为1，修改数字后cnt自减1，当下次再需要修改时，如果cnt已经为0了，直接返回false。遍历结束后返回true


# reference
[[LeetCode] Non-decreasing Array 非递减数列][1]


[1]: http://www.cnblogs.com/grandyang/p/7565424.html