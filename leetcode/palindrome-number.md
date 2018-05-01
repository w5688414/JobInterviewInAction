# problem
>Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.


# codes
```
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int base=1;
        int num=x;
        while(num/10>0){
            base=base*10;
            num=num/10;
        }
        while(x>=10){
            int a1=x/base;
            int b1=x%10;
            if(a1!=b1){
                return false;
            }
            x=x%base;
            x=x/10;
            base=base/100;
        }
        return true;
    }
};
```

# analysis
>把数变为字符串，但不符合题目要求；或者反转整个数都能求解，反转数可能溢出。这里直接求解，我们先比较最高位和最低位，然后相应的比较第二位和次高位，这样循环下去，思路很简答，这里需要求解base，base代表数量级，就是x的第二高的数量级，比如x=10001，base=1000。

# reference
[[编程题]palindrome-number][1]

[1]: https://www.nowcoder.com/questionTerminal/35b8166c135448c5a5ba2cff8d430c32