# problem
>Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

# codes
```
class Solution {
public:
    int atoi(const char *str) {
        int i=0;
        bool is_negative=false;
        while(str[i]==' '&&str[i]!='\0'){
            i++;
        }
        if(str[i]=='+'){
            i++;
        }else if(str[i]=='-'){
            is_negative=true;
            i++;
        }
        long sum=0;
        for(;str[i]!='\0'&&str[i]!=' ';i++){
            if(str[i]>='0'&&str[i]<='9'){
                sum=sum*10+str[i]-'0';
                if(sum>INT_MAX&&is_negative){
                    return INT_MIN;
                }else if(sum>INT_MAX){
                    return INT_MAX;
                }
            }else{
               break;
            }
        }
        if(is_negative){
            return -sum;
        }
        return sum;
    }
};
```

# analysis
>直接法计算，这里要考虑溢出，有空格，非法字符等情况。

# reference
[[编程题]string-to-integer-atoi][1]

[1]: https://www.nowcoder.com/questionTerminal/44d8c152c38f43a1b10e168018dcc13f