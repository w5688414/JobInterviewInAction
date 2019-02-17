# problem
>There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
# codes 1
```
class Solution {
public:
    int candy(vector<int> &ratings) {
        int len=ratings.size();
        vector<int> dp(len,1);
        for(int i=1;i<ratings.size();i++){
            if(ratings[i]>ratings[i-1]){
                dp[i]=dp[i-1]+1;
            }
        }
        for(int i=len-2;i>=0;i--){
            if(ratings[i]>ratings[i+1]&&dp[i]<=dp[i+1]){
                dp[i]=dp[i+1]+1;
            }
        }
        int sum=0;
        for(int i=0;i<len;i++){
            sum+=dp[i];
        }
        return sum;
    }
};

```
# codes 2
```
class Solution {
public:
    int candy(vector<int>& ratings) {
        int n=ratings.size();
        vector<int> nums(n,1);
        for(int i=0;i<n-1;i++){
            if(ratings[i+1]>ratings[i]){
                nums[i+1]=nums[i]+1;
            }
        }
        for(int i=n-1;i>0;i--){
            if(ratings[i-1]>ratings[i]){
                nums[i-1]=max(nums[i-1],nums[i]+1);
            }
        }
        int res=0;
        for(int i=0;i<n;i++){
            res+=nums[i];
        }
        return res;
        
    }
};
```

# analysis
>这道题我感觉不是动态规划，先定义一个技术vector，初始值都为1，然后从左到右，如果遇见当前的rating比前一个相邻的大，就dp[i]=dp[i-1]+1;
然后从右向左，如果遇见当前的rating比后面一个小，且dp[i]<=dp[i+1].求完后遍历求和就是最终的结果。

上面两种解法本质上是一样的。

# reference
[[编程题]candy][1]
[[LeetCode] Candy 分糖果问题][2]
[1]: https://www.nowcoder.com/questionTerminal/74a62e876ec341de8ab5c8662e866aef
[2]:https://www.cnblogs.com/grandyang/p/4575026.html