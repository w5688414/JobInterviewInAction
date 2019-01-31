# problem
> Given two binary strings, return their sum (also a binary string).

For example,
a ="11"
b ="1"
Return"100".

# codes 1
```
class Solution {
public:
    string addBinary(string a, string b) {
        int a1_len=a.length()-1;
        int b1_len=b.length()-1;
        while(a.length()>b.length()){
            b='0'+b;
        }
        while(b.length()>a.length()){
            a='0'+a;
        }
        string s1;
        char flag='0';
        for(int i=a.length()-1;i>=0;i--){
            int ch=a[i]-'0'+b[i]-'0'+flag-'0';
            if(ch==3){
                s1='1'+s1;
                flag='1';
            }else if(ch==2){
                s1='0'+s1;
                flag='1';
            }else{
                char c=ch+'0';
                s1=c+s1;
                flag='0';
            }
        }
        if(flag=='1'){
            s1='1'+s1;
        }
        return s1;
    }
};

```

# analysis 1
>这道题目首先要用0把两个字符串补齐，我开始没想到这个，导致我后面写得很复杂。补齐之后，从最后一位进行二进制的加法运算。

# codes2
```
class Solution {
public:
    string addBinary(string a, string b) {
        stack<int> s;
        int s1=a.length();
        int s2=b.length();
        int i=s1-1;
        int j=s2-1;
        int carry=0;
        while(i>=0||j>=0||carry>0){
            int n1=i>=0 ? a[i--]-'0':0;
            int n2=j>=0 ? b[j--]-'0':0;
            int c=carry+n1+n2;
            s.push(c%2);
            carry=c/2;
        }
        string res="";
        while(!s.empty()){
            res+=s.top()+'0';
            s.pop();
        }
        return res;
    }
};
```
# analysis 2
思路很简单，对a,b从后往前遍历进行加法运算，然后把结果存入栈中，以栈出来的顺序拼接成字符串就是结果了。


# reference
[[编程题]add-binary][1]

[1]: https://www.nowcoder.com/questionTerminal/c8c9f42c19194aa88781efefef4df44b
