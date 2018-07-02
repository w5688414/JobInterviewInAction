# problem
>The string"PAYPALISHIRING"is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line:"PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string text, int nRows);
```
convert("PAYPALISHIRING", 3)should return"PAHNAPLSIIGYIR".


# codes

## s1
```
class Solution {
public:
    string convert(string s, int nRows) {
        if(nRows<=1){
            return s;
        }
        vector<string> zigzag(nRows,"");
        int step=1;
        int row=0;
        for(int i=0;i<s.size();i++){
            zigzag[row]+=s[i];
            if(row==0){
                step=1;
            }else if(row==nRows-1){
                step=-1;
            }
            row+=step;
        }
        string ans;
        for(string temp:zigzag){
            ans+=temp;
        }
        return ans;
    }
};
```

## s2
```
class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows<=1){
            return s;
        }
        string res="";
        int len=2*numRows-2;
        for(int i=0;i<numRows;i++){
            for(int j=i;j<s.size();j+=len){
                res+=s[j];
                int temp=j+len-2*i;
                if(i!=0&&i!=numRows-1&&temp<s.size()){
                    res+=s[temp];
                }
            }
        }
        return res;
    }
};
```

# analysis
## s1
开始碰到这个题目的时候，我是无从下手，可能有了编程恐惧症。后面看了别人的代码，堪称完美的解决了这个问题，上述方法用一个vector维护nRows个字符串，不断的上下移动坐标来维护每个字符串的长度，然后遍历完一遍这个字符串就行了。堪称完美，佩服佩服。

## s2
比如有一个字符串 “0123456789ABCDEF”，转为zigzag
当 n = 2 时：

0 2 4 6 8 A C E

1 3 5 7 9 B D F

当 n = 3 时：

0   4   8   C

1 3 5 7 9 B D F

2   6   A   E

当 n = 4 时：

0      6      C
1    5 7    B D
2  4   8  A   E
3      9      F

除了第一行和最后一行没有中间形成之字型的数字外，其他都有，而首位两行中相邻两个元素的index之差跟行数是相关的，为 2*nRows - 2,
- 根据这个特点，我们可以按顺序找到所有的黑色元素（例如n=4中的第一列）在元字符串的位置，将他们按顺序加到新字符串里面
- 对于红色元素出现的位置也是有规律的，每个红色元素（例如n=4中的第二列）的位置为 j + 2*nRows-2 - 2*i, 其中，j为前一个黑色元素的列数，i为当前行数。
- 比如当n = 4中的那个红色5，它的位置为 1 + 2*4-2 - 2*1 = 5，为原字符串的正确位置。
- 当我们知道所有黑色元素和红色元素位置的正确算法，我们就可以一次性的把它们按顺序都加到新的字符串里面。

# reference
[[编程题]zigzag-conversion][1]
[[LeetCode] ZigZag Converesion 之字型转换字符串][2]

[1]: https://www.nowcoder.com/questionTerminal/d3583975276743d3befe2ddd43156d14
[2]:http://www.cnblogs.com/grandyang/p/4128268.html