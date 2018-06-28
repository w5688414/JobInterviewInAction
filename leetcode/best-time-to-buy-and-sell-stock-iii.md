# problem
> Say you have an array for which the i th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: 
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# codes

## s1
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
## s2
```
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()){
            return 0;
        }
        int n=prices.size();
        int g[n][3]={0};
        int l[n][3]={0};
        for(int i=1;i<n;i++){
            int diff=prices[i]-prices[i-1];
            for(int j=1;j<=2;j++){
                l[i][j]=max(g[i-1][j-1]+max(diff,0),l[i-1][j]+diff);
                g[i][j]=max(l[i][j],g[i-1][j]);
            }
        }
        return g[n-1][2];
    }
};
```

# analysis
>这道题我还不怎么明白其过程，按照参考博客的思路，buy1记录的是所有天最便宜的报价，sell1记录的是所有天只进行1次买卖的最大利益；buy2表示在第一次获得最大利益后，再买到那次交易后最便宜股价是剩余的净利润，sell2记录的是两次完整交易的最大利润。

## s2
这道题目太难，我做不出来，还是硬着头皮抄了一遍。dp不会，硬伤。

这里我们先解释最多可以进行k次交易的算法，然后最多进行两次我们只需要把k取成2即可。我们还是使用“局部最优和全局最优解法”。我们维护两种量，一个是当前到达第i天可以最多进行j次交易，最好的利润是多少（global[i][j]），另一个是当前到达第i天，最多可进行j次交易，并且最后一次交易在当天卖出的最好的利润是多少（local[i][j]）。下面我们来看递推式，全局的比较简单，
            global[i][j]=max(local[i][j],global[i-1][j])，
也就是去当前局部最好的，和过往全局最好的中大的那个（因为最后一次交易如果包含当前天一定在局部最好的里面，否则一定在过往全局最优的里面）。对于局部变量的维护，递推式是
            local[i][j]=max(global[i-1][j-1]+max(diff,0),local[i-1][j]+diff)，
也就是看两个量，第一个是全局到i-1天进行j-1次交易，然后加上今天的交易，如果今天是赚钱的话（也就是前面只要j-1次交易，最后一次交易取当前天），第二个量则是取local第i-1天j次交易，然后加上今天的差值（这里因为local[i-1][j]比如包含第i-1天卖出的交易，所以现在变成第i天卖出，并不会增加交易次数，而且这里无论diff是不是大于0都一定要加上，因为否则就不满足local[i][j]必须在最后一天卖出的条件了）。

# reference
[[编程题]best-time-to-buy-and-sell-stock-iii][1]
[[LeetCode] Best Time to Buy and Sell Stock III 买股票的最佳时间之三][2]
[Best Time to Buy and Sell Stock III -- LeetCode][3]

[1]: https://www.nowcoder.com/questionTerminal/03905f7b819241398b02ee39bef3e8f1
[2]: http://www.cnblogs.com/grandyang/p/4281975.html
[3]: https://blog.csdn.net/linhuanmars/article/details/23236995