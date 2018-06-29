# problem
>In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

Example 1:
```
Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
This poisoned status will last 2 seconds until the end of time point 2. 
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
So you finally need to output 4.
```
Example 2:
```
Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
This poisoned status will last 2 seconds until the end of time point 2. 
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
So you finally need to output 3.
```
Note:
1. You may assume the length of given time series array won't exceed 10000.
2. You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.

# codes
```
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        if(timeSeries.empty()){
            return 0;
        }
        int res=0;
        int n=timeSeries.size();
        for(int i=1;i<n;i++){
            int diff=timeSeries[i]-timeSeries[i-1];
            res+=(diff < duration) ? diff:duration;
        }
        return res+duration;
    }
};
```

# analysis
>直接使用贪心算法，比较相邻两个时间点的时间差，如果小于duration，就加上这个差，如果大于或等于，就加上duration即可.
这道题虽然读懂了，好像不怎么会做了，可能被吓到了吧，希望后面心理素质好一点。

# reference
[[LeetCode] Teemo Attacking 提莫攻击][1]


[1]: http://www.cnblogs.com/grandyang/p/6399408.html
