# problem
> Say you have an array for which the i th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: 
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# codes
```
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int buy1=INT_MIN;
        int sell1=0;
        int buy2=INT_MIN;
        int sell2=0;
        for(int i=0;i<prices.size();i++){ //每次循环表示进入新的一天
            buy1=max(buy1,-prices[i]);  //记录之前所有天最便宜的股价
            sell1=max(sell1,buy1+prices[i]);  //记录之前所有天只进行1次买卖的最大利益
            buy2=max(buy2,sell1-prices[i]);  //记录之前天先进行1次交易获得最大利益后，
                   //再买到那次交易后最便宜股价时剩余的净利润
            sell2=max(sell2,buy2+prices[i]); //记录之前天进行2次完整交易的最大利润
        }
        return sell2;
    }
};
```

# analysis
>这道题我还不怎么明白其过程，按照参考博客的思路，buy1记录的是所有天最便宜的报价，sell1记录的是所有天只进行1次买卖的最大利益；buy2表示在第一次获得最大利益后，再买到那次交易后最便宜股价是剩余的净利润，sell2记录的是两次完整交易的最大利润。

# reference
[[编程题]best-time-to-buy-and-sell-stock-iii][1]

[1]: https://www.nowcoder.com/questionTerminal/03905f7b819241398b02ee39bef3e8f1
