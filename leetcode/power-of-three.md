# problem
> Given an integer, write a function to determine if it is a power of three.

Example 1:
```
Input: 27
Output: true
```
Example 2:
```
Input: 0
Output: false
```
Example 3:
```
Input: 9
Output: true
```
Example 4:
```
Input: 45
Output: false
```
Follow up:
Could you do it without using any loop / recursion?

# codes
```
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n<0){
            return false;
        }
        return int(log10(n)/log10(3))-log10(n)/log10(3)==0;
    }
};
```

# analysis
>这种方法的好处是，它利用了自己上一层构造好的next指针，代码简洁巧妙。

# reference
[[LeetCode] Power of Three 判断3的次方数][1]

[1]: https://www.cnblogs.com/grandyang/p/5138212.html