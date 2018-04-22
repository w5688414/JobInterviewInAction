# problem
>Validate if a given string is numeric.

Some examples:
"0"=>true
" 0.1 "=>true
"abc"=>false
"1 a"=>false
"2e10"=>true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

# codes
```
class Solution {
public:
    bool isNumber(const char *s) {
        if(s==NULL)
            return false;
        int start=0;
        while(s[start]==' '){
            start++;
        }
        bool numeric=scanInteger(s,start);
        if(s[start]=='.'){
            start++;
            numeric=scanUnsignedInteger(s,start)||numeric;
        }
        if(s[start]=='e'||s[start]=='E'){
            start++;
            numeric=numeric&&scanInteger(s,start);
        }
        while(s[start]==' '){
            start++;
        }
        return numeric&&s[start]=='\0';
    }
    
    bool scanInteger(const char *s,int &start){
        if(s[start]=='+'||s[start]=='-'){
            start++;
        }
        return scanUnsignedInteger(s,start);
    }
    
    bool scanUnsignedInteger(const char *s,int &start){
        int i=start;
        while(s[i]!='\0'&&s[i]>='0'&&s[i]<='9'){
            i++;
        }
        bool flag=i>start;
        start=i;
        return flag;
    }
};

```

# analysis
>这道题看似简单，但是没有找到方法却很难做，我参考了leetcode的解法，用.和e E等把字符串分为两部分，然后分开来判断其子字符串是否是数字，如果都是数字并且已经遍历到末尾了，我们就可以认为这个字符串是合法的。

# reference
[[编程题]valid-number][1]
[1]: https://www.nowcoder.com/questionTerminal/608d810765a34df2a0d47645626dd2d3