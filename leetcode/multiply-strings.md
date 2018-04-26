# problem
>Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.


# codes
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

# analysis
>不知道是不是编程思维不好的原因，这是一个模拟乘法的题目，如果是一个数学题目，很简单，用程序模拟出来就需要考虑很多情况，主要方法是举例子说明：128*126
先128上的8与下面的6 2 1分别相乘，结果放在哪儿呢，申请一个3+3=6位的数组，因为三位数乘以三位数，最大是六位数。8*6=48,最高位是8,然后把4保存起来用于下一位的计算，这样移一直下去。

# reference
[[编程题]multiply-strings][1]

[1]: https://www.nowcoder.com/questionTerminal/76a5d7a3173446c2ab34b8c5fe836f1d