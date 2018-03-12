# problem
>定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。

# codes
```
class Solution {
public:
    void push(int value) {
        stack1.push(value);
    }
    void pop() {
        stack1.pop();
    }
    int top() {
        return stack1.top();
    }
    int min() {
        int minValue=stack1.top();
        while(!stack1.empty()){
            if(stack1.top()<minValue)
                minValue=stack1.top();
            stack2.push(stack1.top());
            stack1.pop();
        }
        while(!stack2.empty()){
            stack1.push(stack2.top());
            stack2.pop();
        }
        return minValue;
    }
private:
    stack<int> stack1;
    stack<int> stack2;
};
```
# analysis
>这是对两个栈进行操作的一个题目，push，pop，top的时候，用一个栈来实现就行了。求min的时候
>需要先把这个栈的数据都取出来找到最小的值，然后又把数据放回去。
# reference
[定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。][1]

[1]: https://www.cnblogs.com/wdan2016/p/5945507.html