# problem
>Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

# codes
```
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
private:
    queue<int> q;
    void make_queue(vector<NestedInteger> &nestedList){
        for(auto a:nestedList){
            if(a.isInteger()) q.push(a.getInteger());
            else{
               make_queue(a.getList()); 
            } 
        }
    }
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        make_queue(nestedList);
    }

    int next() {
        int t=q.front();
        q.pop();
        return t;
    }

    bool hasNext() {
        return !q.empty();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```

# analysis
>用队列的形式出现，我开始想到了，但是没有做出来，没有挖掘出来题目的一些隐藏的函数，没想到一个递归就能解决，看来自己还需要磨练。
  

# reference
[[LeetCode] Flatten Nested List Iterator 压平嵌套链表迭代器][1]
[1]: http://www.cnblogs.com/grandyang/p/5358793.html
