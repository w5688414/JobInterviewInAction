# problem
>Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

- void addNum(int num) - Add a integer number from the data stream to the data structure.
- double findMedian() - Return the median of all elements so far.

Example:
```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```

# codes
```
class MedianFinder {
private:
    priority_queue<int> large,small;
public:
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        small.push(num);
        large.push(-small.top());
        small.pop();
        while(small.size()<large.size()){
            small.push(-large.top());
            large.pop();
        }
    }
    
    double findMedian() {
        if(small.size()>large.size()){
            return small.top();
        }else{
            return 0.5*(small.top()-large.top());
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
```

# analysis
>我们使用大小堆来解决问题，其中大堆保存右半段较大的数字，小堆保存左半段较小的数组。这样整个数组就被中间分为两段了，由于堆的保存方式是由大到小，我们希望大堆里面的数据是从小到大，这样取第一个来计算中位数方便。我们用到一个小技巧，就是存到大堆里的数先取反再存，这样由大到小存下来的顺序就是实际上我们想要的从小到大的顺序。当大堆和小堆中的数字一样多时，我们取出大堆小堆的首元素求平均值，当小堆元素多时，取小堆首元素为中位数.

 这是一个hard题目，我做不出来。

# reference
[[LeetCode] Find Median from Data Stream 找出数据流的中位数][1]

[1]: http://www.cnblogs.com/grandyang/p/4896673.html