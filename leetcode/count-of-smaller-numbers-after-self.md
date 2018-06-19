# problem
>You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
Example:
```
Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

# codes
```
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> res(nums.size(),0);
        vector<int> t;
        for(int i=nums.size()-1;i>=0;i--){
            int left=0;
            int right=t.size();
            while(left<right){
                int mid=(left+right)/2;
                if(nums[i]>t[mid]){
                    left=mid+1;
                }else{
                    right=mid;
                }
            }
            res[i]=right;
            t.insert(t.begin()+right,nums[i]);
        }
        return res;
    }
};
```

# analysis
>这道题的思路我也没想出来，我想的是从前往后，没发现从后往前遍历就很好解决了。看来自己的思维能力还需要历练。

首先可以使用用二分搜索法，思路是将给定数组从最后一个开始，用二分法插入到一个新的数组，这样新数组就是有序的，那么此时该数字在新数组中的坐标就是原数组中其右边所有较小数字的个数

# reference

[[LeetCode] Count of Smaller Numbers After Self 计算后面较小数字的个数][1]

[1]: https://www.cnblogs.com/grandyang/p/5078490.html
