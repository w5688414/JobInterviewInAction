# problem
>The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return[0,1,3,2]. Its gray code sequence is:
```
00 - 0
01 - 1
11 - 3
10 - 2
```
Note: 
For a given n, a gray code sequence is not uniquely defined.

For example,[0,2,3,1]is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

# codes
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

# analysis
- 当n=1时，为[0,1]
- 当n=2时，为[00,01,11,10]
- 当n=3时，为[000,001,011,010,110,111,101,100]
- 由此可以看出新的序列其实是在前面序列基础上插入新的值
其中前半部分的数值不变，后半部分的数值为上个序列中每个元素第n个位变1，逆向插入
# reference
[[编程题]gray-code][1]

[1]: https://www.nowcoder.com/questionTerminal/55dddb4cdf074fefba653ff523e42346