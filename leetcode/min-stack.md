# problem
>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

# codes

```
class MinStack {
private:
    stack<int> s1,s2;
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        s1.push(x);
        if(s2.empty()||x<=s2.top()){
            s2.push(x);
        }
    }
    
    void pop() {
        if(s1.top()==s2.top()) s2.pop();
        s1.pop();
    }
    
    int top() {
        return s1.top();
    }
    
    int getMin() {
        return s2.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

# analysis
>这虽然是一个容易题，但是我没有做出来，最小栈只不过在原有栈的基础上增加了一个获取最小值的功能，我们可以用两个栈来模拟，第一个栈来模拟正常的栈的功能，第二个栈用来存储栈中的最小值。注意我们在pop和push的一点小小的改变。


# reference
[[LeetCode] Min Stack 最小栈][1]
[1]: https://www.cnblogs.com/grandyang/p/4091064.html
