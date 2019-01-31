# problem
> Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
```
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
```
Example 2:
```
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
```
Note:
1. The n and k are in the range 1 <= k < n <= 10^4.

# codes
```
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> res;
        int i=1;
        int j=n;
        while(i<=j){
            if(k>1){
                if(k%2==1){
                    res.push_back(i);
                    i++;
                }else{
                    res.push_back(j);
                    j--;
                }
                k--;
            }else{
                res.push_back(i++);
            }
        }
        return res;
    }
};
```

# analysis
>题目的大致意思是：给你一个整数的返回n，和一个k，然后把这n个数排成一圈，然后相邻见的差值的种类数为k，然后输出这样一个序列。

- 比如说当n=8，我们有数组：

1, 2, 3, 4, 5, 6, 7, 8

当我们这样有序排列的话，相邻两数的差的绝对值为1。我们想差的绝对值最大能为多少，应该是把1和8放到一起，为7。那么为了尽可能的产生不同的差的绝对值，我们在8后面需要放一个小数字，比如2，这样会产生差的绝对值6，同理，后面再跟一个大数，比如7，产生差的绝对值5，以此类推，我们得到下列数组：

1, 8, 2, 7, 3, 6, 4, 5

其差的绝对值为：7，6，5，4，3，2，1

共有7种，所以我们知道k最大为n-1，所以这样的排列一定会存在。我们的策略是，先按照这种最小最大数相邻的方法排列，没排一个，k自减1，当k减到1的时候，后面的排列方法只要按照生序的方法排列，就不会产生不同的差的绝对值，这种算法的时间复杂度是O(n)，属于比较高效的那种。我们使用两个指针，初始时分别指向1和n，然后分别从i和j取数加入结果res，每取一个数字k自减1，直到k减到1的时候，开始按升序取后面的数字

# reference
[[LeetCode] Beautiful Arrangement II 优美排列之二][1]

[1]: http://www.cnblogs.com/grandyang/p/7577878.html