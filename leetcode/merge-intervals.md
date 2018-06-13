# problem
>Given a collection of intervals, merge all overlapping intervals.

For example,
Given[1,3],[2,6],[8,10],[15,18],
return[1,6],[8,10],[15,18].

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
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> result;
        if(intervals.size()==0){
            return result;
        }
        sort(intervals.begin(),intervals.end(),[](Interval &a,Interval &b){
            return a.start<b.start;
        });
        Interval newInterval=intervals[0];
        for(int i=1;i<intervals.size();i++){
            if(newInterval.end>=intervals[i].start){
                newInterval.start=min(newInterval.start,intervals[i].start);
                newInterval.end=max(newInterval.end,intervals[i].end);
            }else{
                result.push_back(newInterval);
                newInterval=intervals[i];
            }
        }
        result.push_back(newInterval);
        return result;
    }
};
```

# analysis
>这主要是在遍历之前需要做一下排序，排序的话，注意compare函数需要放在类的外面才行，下面没什么好说的，一次遍历，满足条件就行了。
开始我开在了由多个交叉区间怎么进行合并，原来重新newInterval来不断的循环判断就行了，没有交叉就把它存下来。

# reference
[[编程题]merge-intervals][1]
[[LeetCode] Merge Intervals 合并区间][2]

[1]: https://www.nowcoder.com/questionTerminal/69f4e5b7ad284a478777cb2a17fb5e6a
[2]: https://www.cnblogs.com/grandyang/p/4370601.html
