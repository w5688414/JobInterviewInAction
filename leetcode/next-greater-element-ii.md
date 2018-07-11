# problem
>Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
```
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
```
Note: The length of given array won't exceed 10000.

# codes
```
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n=nums.size();
        vector<int> res(n,-1);
        stack<int> s;
        for(int i=0;i<2*n;i++){
            int num=nums[i%n];
            while(!s.empty()&&nums[s.top()]<num){
                res[s.top()]=num;
                s.pop();
            }
            if(i<n) s.push(i);
        }
        return res;
    }
};
```

# analysis
>我们遍历两倍的数组，然后还是坐标i对n取余，取出数字，如果此时栈不为空，且栈顶元素小于当前数字，说明当前数字就是栈顶元素的右边第一个较大数，那么建立二者的映射，并且去除当前栈顶元素，最后如果i小于n，则把i压入栈。因为res的长度必须是n，超过n的部分我们只是为了给之前栈中的数字找较大值，所以不能压入栈。

原来是循环查找，我想多了，然后做着不对。

# reference
[[LeetCode] Next Greater Element II 下一个较大的元素之二][1]

[1]: http://www.cnblogs.com/grandyang/p/6442861.html