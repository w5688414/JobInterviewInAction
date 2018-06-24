# problem
>Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example :
```
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

# codes
```
class Solution {
public:
    bool isHappy(int n) {
        set<int> s;
        while(n!=1){
            int t=0;
            while(n>0){
                t+=(n%10)*(n%10);
                n=n/10;
            }
            n=t;
            if(s.count(t)){
                break;
            }else{
                s.insert(t);
            }
        }
        return n==1;
    }
};
```

# analysis
- 这道题算是一个容易题，关键是怎么判断循环的存在，这里用了一个set存放已经出现过的数字，所以后面只需要判断数字在set是否出现过就可以判断是否有循环了，如果有循环，则数字一定会在set里面再出现，这样就找到了终止条件了。

# reference
[[LeetCode] Happy Number 快乐数][1]

[1]: http://www.cnblogs.com/grandyang/p/4447233.html
