# problem
>Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().
Example:
```
Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
```
Follow up: How would you extend your design to be generic and work with all types, not just integer?

# codes
```
// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.
class Iterator {
    struct Data;
	Data* data;
public:
	Iterator(const vector<int>& nums);
	Iterator(const Iterator& iter);
	virtual ~Iterator();
	// Returns the next element in the iteration.
	int next();
	// Returns true if the iteration has more elements.
	bool hasNext() const;
};


class PeekingIterator : public Iterator {
private:
    bool flag;
    int value;
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    flag=false;
	}

    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
      if(!flag){
          value=Iterator::next();
          flag=true;
      }
        return value;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    if(!flag) return Iterator::next();
        flag=false;
        return value;
	}

	bool hasNext() const {
	    if(flag) return true;
        if(Iterator::hasNext()) return true;
        return false;
	}
};
```

# analysis
>这道题让我们实现一个顶端迭代器，在普通的迭代器类Iterator的基础上增加了peek的功能，就是返回查看下一个值的功能，但是不移动指针，next()函数才会移动指针，那我们可以定义一个变量专门来保存下一个值，再用一个bool型变量标记是否保存了下一个值，再调用原来的一些成员函数，就可以实现这个顶端迭代器了.

# reference
[[LeetCode] Peeking Iterator 顶端迭代器][1]

[1]: http://www.cnblogs.com/grandyang/p/4825068.html