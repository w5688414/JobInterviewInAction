# problem
> Say you have an array for which the i th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# codes
```
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sum=0;
        for(int i=1;i<prices.size();i++){
            if(prices[i]>prices[i-1]){
                sum+=prices[i]-prices[i-1];
            }
        }
        return sum;
    }
};

```

# analysis
>看来编程题目需要分析一下，思路没有理清，很费劲，因为可以交易多次，如果股价呈现递增的趋势，就可以盈利，然后就可以交易。

# reference
[[编程题]best-time-to-buy-and-sell-stock-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/572903b1edbd4a33b2716f7649b4ffd4
