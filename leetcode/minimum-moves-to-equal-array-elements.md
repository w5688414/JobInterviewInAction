# problem
>Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:
```
Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
```

# codes
```
class Solution {
public:
    int minMoves(vector<int>& nums) {
        int min_val=INT_MAX;
        for(int num:nums){
            min_val=min(min_val,num);
        }
        int sum=0;
        for(int num:nums){
            sum+=num-min_val;
        }
        return sum;
    }
};
```

# analysis
>需要换一个角度来看问题，其实给n-1个数字加1，效果等同于给那个未被选中的数字减1;
- 比如数组[1，2，3], 给除去最大值的其他数字加1，变为[2，3，3]，我们全体减1，并不影响数字间相对差异，变为[1，2，2]，这个结果其实就是原始数组的最大值3自减1;
- 那么问题也可能转化为，将所有数字都减小到最小值，这样难度就大大降低了，我们只要先找到最小值，然后累加每个数跟最小值之间的差值即可.

# reference
[[LeetCode] Minimum Moves to Equal Array Elements 最少移动次数使数组元素相等][1]

[1]: http://www.cnblogs.com/grandyang/p/6053827.html