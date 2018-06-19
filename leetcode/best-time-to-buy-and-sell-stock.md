# problem
>Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```
Example 2:
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

# codes
```
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()==0){
            return 0;
        }
        int minprice=prices[0];
        int maxprofit=0;
        for(int i=1;i<prices.size();i++){
            if(prices[i]<minprice){
                minprice=prices[i];
            }
            maxprofit=max(prices[i]-minprice,maxprofit);
        }
        return maxprofit;
    }
};
```

# analysis
>无论你怎么交易，我们只需要再价格最少的那一天买进，然后在后面的价格最大的一天卖出就行了，然后我们用minprice和maxprofit两个来表示最小价格和最大收益。然后不断更新最小价格和最大收益就行了。

# reference
[121. Best Time to Buy and Sell Stock][1]

[1]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/