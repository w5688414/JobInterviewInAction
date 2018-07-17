# problem
> Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.
Example:
```
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
```

# codes
```
class Solution {
private:
    vector<int> v;
public:
    Solution(vector<int> nums):v(nums) {
        
    }
    
    int pick(int target) {
        int cnt=0,res=-1;
        for(int i=0;i<v.size();i++){
            if(v[i]!=target) continue;
            ++cnt;
            if(rand()%cnt==0) res=i;
        }
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
```

# analysis
>水塘抽样算法，没什么好说的，不懂算法就不会做。

# reference
[[LeetCode] Random Pick Index 随机拾取序列][1]


[1]: http://www.cnblogs.com/grandyang/p/5875509.html