# problem
>Given a list of non negative integers, arrange them such that they form the largest number.
Example 1:
```
Input: [10,2]
Output: "210"
```
Example 2:
```
Input: [3,30,34,5,9]
Output: "9534330"
```
Note: The result may be very large, so you need to return a string instead of an integer.

# codes
```
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        string res;
        sort(nums.begin(),nums.end(),[](int a,int b){
           return to_string(a)+to_string(b)> to_string(b)+to_string(a); 
        });
        for(int i=0;i<nums.size();i++){
            res+=to_string(nums[i]);
        }
        return res[0]=='0' ? "0":res;
    }
};
```

# analysis
>这道题我倒是没想出来要重写sort函数来排序，然后把排序结果都拼接起来就行了。


# reference
[[LeetCode] Largest Number 最大组合数][1]

[1]: http://www.cnblogs.com/grandyang/p/4225047.html