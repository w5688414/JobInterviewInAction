# problem
>Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
```
Input:
3

Output:
3
```
Example 2:
```
Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
```


# codes

## s1
```
class Solution {
public:
    int findNthDigit(int n) {
        long len=1,cnt=9,start=1;
        while(n>cnt*len){
            n-=cnt*len;
            cnt=cnt*10;
            start=start*10;
            len++;
        }
        start+=(n-1)/len;
        string t=to_string(start);
        return t[(n-1)%len]-'0';
    }
};
```

# analysis
>这道题我的方法超时，我没有做出来，发现还是找规律的题目。
- 我们首先来分析自然数序列和其位数的关系，前九个数都是1位的，然后10到99总共90个数字都是两位的，100到999这900个数都是三位的，那么这就很有规律了；
- 我们可以定义个变量cnt，初始化为9，然后每次循环扩大10倍，再用一个变量len记录当前循环区间数字的位数；
- 另外再需要一个变量start用来记录当前循环区间的第一个数字，我们n每次循环都减去len*cnt (区间总位数)，当n落到某一个确定的区间里了，那么(n-1)/len就是目标数字在该区间里的坐标，加上start就是得到了目标数字，然后我们将目标数字start转为字符串，(n-1)%len就是所要求的目标位。

数学不好就做不出来，需要多一点历练。

# reference
[[LeetCode] Nth Digit 第N位][1]


[1]: http://www.cnblogs.com/grandyang/p/5891871.html