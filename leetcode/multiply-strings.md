# problem
>Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.


# codes

## s1
```
class Solution {
public:
    string multiply(string num1, string num2) {
        int carry=0;
        string result(num1.size()+num2.size(),'0');
        for(int i=num1.size()-1;i>=0;i--){
            int a=num1[i]-'0';
            for(int j=num2.size()-1;j>=0;j--){
                int b=a*(num2[j]-'0');
                int c=b+carry+result[i+j+1]-'0';
                result[i+j+1]=c%10+'0';
                carry=c/10;
            }
            if(carry>0){
                result[i]=carry+'0';
                carry=0;
            }
        }
        int i=0;
        while(i<result.size()&&result[i]=='0'){
            i++;
        }
        
        return i==result.size() ? "0": result.substr(i);
    }
};
```
## s2

```
class Solution {
public:
    string multiply(string num1, string num2) {
        string res="";
        int m=num1.size();
        int n=num2.size();
        vector<int> v(m+n,0);
        int k=m+n-2;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                v[k-i-j]+=(num1[i]-'0')*(num2[j]-'0');
            }
        }
        int carry=0;
        for(int i=0;i<m+n;i++){
            v[i]+=carry;
            carry=v[i]/10;
            v[i]=v[i]%10;
        }
        int i=m+n-1;
        while(v[i]==0){
            i--;
        }
        if(i<0){
            return "0";
        }
        while(i>=0) res.push_back(v[i--]+'0');
        return res;
    }
};
```

# analysis
## s1
不知道是不是编程思维不好的原因，这是一个模拟乘法的题目，如果是一个数学题目，很简单，用程序模拟出来就需要考虑很多情况，主要方法是举例子说明：128*126
先128上的8与下面的6 2 1分别相乘，结果放在哪儿呢，申请一个3+3=6位的数组，因为三位数乘以三位数，最大是六位数。8*6=48,最高位是8,然后把4保存起来用于下一位的计算，这样移一直下去。
## s2
把错位相加后的结果保存到一个一维数组中，然后分别每位上算进位，最后每个数字都变成一位，然后要做的是去除掉首位0，最后把每位上的数字按顺序保存到结果中即可

# reference
[[编程题]multiply-strings][1]
[[LeetCode] Multiply Strings 字符串相乘][2]

[1]: https://www.nowcoder.com/questionTerminal/76a5d7a3173446c2ab34b8c5fe836f1d
[2]: http://www.cnblogs.com/grandyang/p/4395356.html