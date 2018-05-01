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

# analysis
>开始碰到这个题目的时候，我是无从下手，可能有了编程恐惧症。后面看了别人的代码，堪称完美的解决了这个问题，上述方法用一个vector维护nRows个字符串，不断的上下移动坐标来维护每个字符串的长度，然后遍历完一遍这个字符串就行了。堪称完美，佩服佩服。

# reference
[[编程题]zigzag-conversion][1]

[1]: https://www.nowcoder.com/questionTerminal/d3583975276743d3befe2ddd43156d14