# problem
>Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
```
Input: [3,2,3]
Output: [3]
```
Example 2:
```
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```

# codes

## s1
```
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> res;
        int m=0;
        int n=0;
        int cm=0;
        int cn=0;
        for(auto a:nums){
            if(a==m){
                cm++;
            }else if(a==n){
                cn++;
            }else if(cm==0){
                m=a;
                cm=1;
            }else if(cn==0){
                n=a;
                cn=1;
            }else{
                cm--;
                cn--;
            }
        }
        cm=0;
        cn=0;
        for(auto a:nums){
            if(a==m) cm++;
            else if(a==n) cn++;
        }
        if(cm>nums.size()/3) res.push_back(m);
        if(cn>nums.size()/3) res.push_back(n);
        return res;
    }
};
```


# analysis
>让我们先考虑可能会有多少个众数，经过举了很多例子分析得出，任意一个数组出现次数大于n/3的众数最多有两个。那么有了这个信息，我们使用投票法的核心是找出两个候选众数进行投票，需要两遍遍历，第一遍历找出两个候选众数，第二遍遍历重新投票验证这两个候选众数是否为众数即可，选候选众数方法和前面那篇Majority Element 求众数一样，由于之前那题题目中限定了一定会有众数存在，故而省略了验证候选众数的步骤，这道题却没有这种限定，即满足要求的众数可能不存在，所以要有验证。


# reference
[[LeetCode] Majority Element II 求众数之二][1]


[1]: http://www.cnblogs.com/grandyang/p/4606822.html