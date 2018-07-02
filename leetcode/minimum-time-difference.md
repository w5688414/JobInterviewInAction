# problem
>Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
```
Input: ["23:59","00:00"]
Output: 1
```
Note:
1. The number of time points in the given list is at least 2 and won't exceed 20000.
2. The input time is legal and ranges from 00:00 to 23:59.


# codes
```
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int res=INT_MAX;
        int n=timePoints.size();
        sort(timePoints.begin(),timePoints.end());
        for(int i=0;i<n;i++){
            string t1=timePoints[i];
            string t2=timePoints[(i+1)%n];
            int h1=(t1[0]-'0')*10+t1[1]-'0';
            int m1=(t1[3]-'0')*10+t1[4]-'0';
            int h2=(t2[0]-'0')*10+t2[1]-'0';
            int m2=(t2[3]-'0')*10+t2[4]-'0';
            int diff=(h2-h1)*60+m2-m1;
            if(i==n-1) diff+=24*60;
            res=min(res,diff);
        }
        return res;
    }
};
```

# analysis
>那么最简单直接的办法就是给数组排序，这样时间点小的就在前面了，然后我们分别把小时和分钟提取出来，计算差值，注意唯一的特殊情况就是第一个和末尾的时间点进行比较，第一个时间点需要加上24小时再做差值.

# reference
[[LeetCode] Minimum Time Difference 最短时间差][1]

[1]: http://www.cnblogs.com/grandyang/p/6568398.html