# problem
>Shuffle a set of numbers without duplicates.

Example:
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

# codes
```
class Solution {
private:
    vector<int> v;
public:
    Solution(vector<int> nums):v(nums) {
        
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return v;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> res=v;
        int n=v.size();
        for(int i=0;i<n;i++){
            int j=i+rand()%(n-i);
            swap(res[i],res[j]);
        }
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */
```

# analysis
>在随机产生一个序列的时候, 遍历每一个元素, 并且随机一个从他开始的位置与这个位置交换, 这样任意一个元素随机到任意一个位置的概率都是1/n!.

# reference
[[leetcode] 384. Shuffle an Array 解题报告][1]
[[LeetCode] Shuffle an Array 数组洗牌][2]

[1]: https://blog.csdn.net/qq508618087/article/details/52295792
[2]: http://www.cnblogs.com/grandyang/p/5783392.html
