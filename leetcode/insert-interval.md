# problem
>
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1: 
Given intervals[1,3],[6,9], insert and merge[2,5]in as[1,5],[6,9].

Example 2: 
Given[1,2],[3,5],[6,7],[8,10],[12,16], insert and merge[4,9]in as[1,2],[3,10],[12,16].

This is because the new interval[4,9]overlaps with[3,5],[6,7],[8,10].

# codes
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
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        vector<Interval> result;
        int i=0;
        for(;i<intervals.size();i++){
            if(newInterval.end<intervals[i].start){
                break;
            }else if(newInterval.start>intervals[i].end){
                result.push_back(intervals[i]);
            }else{
                newInterval.start=min(newInterval.start,intervals[i].start);
                newInterval.end=max(newInterval.end,intervals[i].end);
            }
        }
        result.push_back(newInterval);
        for(;i<intervals.size();i++){
            result.push_back(intervals[i]);
        }
        return result;
    }
};

```

# analysis
> 开始的时候我被这个题目给吓到了，看来心理素质还是有待提升，很简单的一个题目，只需要遍历一边，求插入区间的最大覆盖区间就行了
# reference
[[编程题]insert-interval][1]

[1]: https://www.nowcoder.com/questionTerminal/02418bfb82d64bf39cd76a2902db2190