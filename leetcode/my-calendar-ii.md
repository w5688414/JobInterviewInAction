# problem
>Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:
```
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation: 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
```
Note:
- The number of calls to MyCalendar.book per test case will be at most 1000.
- In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

# codes
```
class MyCalendarTwo {
private:
    set<pair<int,int>> s1,s2;
public:
    MyCalendarTwo() {
        
    }
    
    bool book(int start, int end) {
        for(auto a:s2){
            if(start>=a.second||end<=a.first){
                continue;
            }else{
                return false;
            }
        }
        for(auto a:s1){
            if(start>=a.second||end<=a.first){
                continue;
            }else{
                s2.insert({max(a.first,start),min(a.second,end)});
            }
        }
        s1.insert({start,end});
        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * bool param_1 = obj.book(start,end);
 */
```

# analysis
>我们用两个集合来模拟，其中一个集合来存交集的，另一个集合来村完整的区间的。我们在判断的时候，只需要判断是否跟交集有重叠就行了。
比如事件A，B，C互不重叠，但是有一个事件D，和这三个事件都重叠，这样是可以的，因为重叠的区域最多只有两个。所以关键还是要知道具体的重叠区域，如果两个事件重叠，那么重叠区域就是它们的交集，求交集的方法是两个区间的起始时间中的较大值，到结束时间中的较小值。

# reference
[[LeetCode] My Calendar II 我的日历之二][1]

[1]: http://www.cnblogs.com/grandyang/p/7968035.html