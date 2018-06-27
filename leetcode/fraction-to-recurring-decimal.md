# problem
>Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
```
Input: numerator = 1, denominator = 2
Output: "0.5"
```
Example 2:
```
Input: numerator = 2, denominator = 1
Output: "2"
```
Example 3:
```
Input: numerator = 2, denominator = 3
Output: "0.(6)"
```

# codes
```
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if(numerator==0) return "0";
        string result="";
        if(numerator<=0^denominator<=0) result+="-";
        long long num=abs((long long)numerator);
        long long den=abs((long long)denominator);
        result+=to_string(num/den);
        num=num%den;
        if(num==0){
            return result;
        }else{
            result+=".";
        }
        unordered_map<int,int> map;
        while(num){
            if(map.find(num)!=map.end()){
                result.insert(map[num],1,'(');
                result+=')';
                break;
            }
            map[num]=result.size();
            num=num*10;
            result+=to_string(num/den);
            num=num%den;
            
        }
        return result;
        
    }
};
```

# analysis
>这道题的关键是判断小数的无限循环，这里用了一个hash表来存放分子除法的每一个余数，如果出现余数一样了，说明存在循环了，我们把循环部分插入一个括号就行了。这道题我感觉还是蛮难的，毕竟既要考虑溢出，正负号，又要考虑循环。

# reference
[【leetcode 哈希表】Fraction to Recurring Decimal][1]
[1]: https://blog.csdn.net/u012162613/article/details/41998617
