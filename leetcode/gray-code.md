# problem
>The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:
```
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
```
Example 2:
```
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
```

# codes
## s1
```
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result(pow(2,n));
        for(int i=1;i<=n;i++){
            int size=1<<i;
            int flag=1<<(i-1);
            int index=0;
            for(int j=size-1;2*j>=size;j--){
                result[j] = result[index++]|flag;  //左部插入1
            }
        }
        return result;
    }
};
```
## s2
```
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res;
        for(int i=0;i<pow(2,n);i++){
            res.push_back((i>>1)^i);
        }
        return res;
    }
};
```

# analysis
## s1
- 当n=1时，为[0,1]
- 当n=2时，为[00,01,11,10]
- 当n=3时，为[000,001,011,010,110,111,101,100]
- 由此可以看出新的序列其实是在前面序列基础上插入新的值
其中前半部分的数值不变，后半部分的数值为上个序列中每个元素第n个位变1，逆向插入
## s2
重新做了一下，发现了一个更简单的解法
# reference
[[编程题]gray-code][1]
[[LeetCode] Gray Code 格雷码][2]

[1]: https://www.nowcoder.com/questionTerminal/55dddb4cdf074fefba653ff523e42346
[2]: http://www.cnblogs.com/grandyang/p/4315649.html