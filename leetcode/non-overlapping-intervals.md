# problem
>Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Note:
1. You may assume the interval's end point is always bigger than its start point.
2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
```
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```
Example 2:
```
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```
Example 3:
```
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

# codes

## s1
```
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int eraseOverlapIntervals(vector<Interval>& intervals) {
        int res=0;
        int n=intervals.size();
        sort(intervals.begin(),intervals.end(),[](Interval a,Interval b){
            return a.start<b.start;
        });
        int last=0;
        for(int i=1;i<n;i++){
            if(intervals[i].start<intervals[last].end){
                res++;
                if(intervals[i].end<intervals[last].end) last=i;
            }else{
                last=i;
            }
        }
        return res;
    }
};

```

# analysis
>解法我想不到，首先做一个排序。
判断方法是看如果前一个区间的end大于后一个区间的start，那么一定是重复区间，此时我们结果res自增1，我们需要删除一个，那么此时我们究竟该删哪一个呢，为了保证我们总体去掉的区间数最小，我们去掉那个end值较大的区间，而在代码中，我们并没有真正的删掉某一个区间，而是用一个变量last指向上一个需要比较的区间，我们将last指向end值较小的那个区间；如果两个区间没有重叠，那么此时last指向当前区间，继续进行下一次遍历。


# reference
[[LeetCode] Non-overlapping Intervals 非重叠区间][1]


[1]: http://www.cnblogs.com/grandyang/p/6017505.html