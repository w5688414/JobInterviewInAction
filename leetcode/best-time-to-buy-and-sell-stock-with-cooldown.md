# problem
> Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
```
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

# codes
```
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()==0){
            return 0;
        }
        int len=prices.size();
        vector<int> buy(len+1,0),sell(len+1,0);
        buy[1]=-prices[0];
        for(int i=2;i<=len;i++){
            buy[i]=max(buy[i-1],sell[i-2]-prices[i-1]);
            sell[i]=max(sell[i-1],buy[i-1]+prices[i-1]);
        }
        return sell[len];
    }
};
```

# analysis
1. 在第i天买一支股票还能剩下的利润＝第(i-2)天销售能够剩余的利润－第i天股票的价钱．
2. 在第i天卖一支股票总的利润＝第(i-1)天买股票剩下的最大利润＋当前股票的价格．
也就是说需要维护两个状态的信息，一个是买股票所得到的剩余最大利润，一个是卖出股票之后得到的最大利润，他们互相依赖对方的信息．
对于买来说，当天是否买取决于买了之后是否比之前买所剩余的利润大，即状态转移方程为：

buy[i] = max(buy[i-1], sell[i-2] - prices[i-1]);

对于卖来说，同样当天是否将这只股票卖掉取决于卖掉能否获得更大的利润，状态转移方程为：

sell[i] = max(sell[i-1], buy[i-1] + prices[i-1]);

# reference
[[leetcode] 309. Best Time to Buy and Sell Stock with Cooldown 解题报告][1]
[[LeetCode] Best Time to Buy and Sell Stock with Cooldown 买股票的最佳时间含冷冻期][2]

[1]: https://blog.csdn.net/qq508618087/article/details/51671504
[2]: https://www.cnblogs.com/grandyang/p/4997417.html
