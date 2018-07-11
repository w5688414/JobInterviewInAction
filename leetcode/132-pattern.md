# problem
> Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.
Example 1:
```
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
```
Example 2:
```
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
```
Example 3:
```
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
```
# codes

## s1
```
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int third=INT_MIN;
        stack<int> s;
        for(int i=nums.size()-1;i>=0;i--){
            if(nums[i]<third) return true;
            else{
                while(!s.empty()&&nums[i]>s.top()){
                    third=s.top();
                    s.pop();
                }
            }
            s.push(nums[i]);
        }
        return false;
    }
};
```

# analysis
>我们维护一个栈和一个变量third，其中third就是第三个数字，也是pattern 132中的2，栈里面按顺序放所有大于third的数字，也是pattern 132中的3，那么我们在遍历的时候，如果当前数字小于third，即pattern 132中的1找到了，我们直接返回true即可，因为已经找到了，注意我们应该从后往前遍历数组.

# reference
[[LeetCode] 132 Pattern 132模式][1]

[1]: http://www.cnblogs.com/grandyang/p/6081984.html