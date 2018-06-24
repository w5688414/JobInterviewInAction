# problem
> Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
```
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```
Note:
- 0 < prices.length <= 50000.
- 0 < prices[i] < 50000.
- 0 <= fee < 50000.

# codes
```
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int n=prices.size();
        vector<int> buy(n,0);
        vector<int> sell(n,0);
        buy[0]=-prices[0];
        for(int i=1;i<n;i++){
            buy[i]=max(buy[i-1],sell[i-1]-prices[i]);
            sell[i]=max(sell[i-1],buy[i-1]+prices[i]-fee);
        }
        return sell.back();
    }
};
```

# analysis
sell[i]表示第i天卖掉股票此时的最大利润，buy[i]表示第i天保留手里的股票此时的最大利润
- 在第i天，我们要卖掉手中的股票，那么此时的利润是前一天手里有股票的利润+此时卖掉股票的价格+交易费用；跟前一天卖出的利润相比，取较大值。如果前一天的利润较大，那么我们就在前一天卖了，不留在今天了。
- 如果第i天不卖的利润，就是昨天股票卖了的利润然后今天再买入股票，得减去今天的价格，得到的值和昨天股票保留时的利润相比，取其中的较大值，如果昨天保留股票的利润大，那么我们就继续保留到今天，所以递推时可以得到：

sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee);

buy[i] = max(buy[i - 1], sell[i - 1] - prices[i]);


# reference
[[LeetCode] Best Time to Buy and Sell Stock with Transaction Fee 买股票的最佳时间含交易费][1]

[1]: http://www.cnblogs.com/grandyang/p/7776979.html

