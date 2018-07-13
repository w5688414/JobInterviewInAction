# problem
>The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
```
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
```
Note:
1. Elements of the given array are in the range of 0 to 10^9
2. Length of the array will not exceed 10^4.

# codes
```
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int res=0;
        int n=nums.size();
        for(int i=0;i<32;i++){
            int cnt=0;
            for(int num:nums){
                if(num&(1<<i)){
                    cnt++;
                }
            }
            res+=cnt*(n-cnt);
        }
        return res;
    }
};
```

# analysis
>例子，4，14，2和1：

4:     0 1 0 0

14:   1 1 1 0

2:     0 0 1 0

1:     0 0 0 1
根据规律，我们只需要统计每一列中1的个数，0的个数，然后相乘，然后加入结果res中，就是答案了。
# reference
[[LeetCode] Total Hamming Distance 全部汉明距离][1]

[1]: http://www.cnblogs.com/grandyang/p/6208062.html