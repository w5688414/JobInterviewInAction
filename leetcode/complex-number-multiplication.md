# problem
>Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
Example 1:
```
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
```
Example 2:
```
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
```

Note:

1. The input strings will not have extra blank.
2. The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

# codes
```
class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        int n1=a.length();
        int n2=b.length();
        auto p1=a.find_last_of("+");
        auto p2=b.find_last_of("+");
        int a1=stoi(a.substr(0,p1));
        int b1=stoi(b.substr(0,p2));
        int a2=stoi(a.substr(p1+1,n1-p1-2));
        int b2=stoi(b.substr(p2+1,n2-p2-2));
        int r1=a1*b1-a2*b2;
        int r2=a1*b2+a2*b1;
        string res="";
        res=to_string(r1)+"+"+to_string(r2)+"i";
        return res;
    }
};
```

# analysis
>我们需要把字符串中的实部和虚部分离开并进行运算，那么我们可以用STL中自带的find_last_of函数来找到加号的位置，然后分别拆出实部虚部，进行运算后再变回字符串.

又学习了一个找字符串索引的函数，这道题我也没做出来，估计是被吓到了吧。

# reference
[[LeetCode] Complex Number Multiplication 复数相乘][1]


[1]: http://www.cnblogs.com/grandyang/p/6660437.html