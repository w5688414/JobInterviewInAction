# problem 1
>Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

# codes
```
class Solution {
public:
    int romanToInt(string s) {
        map<char,int> mp;
        mp['I']=1;
        mp['V']=5;
        mp['X']=10;
        mp['L']=50;
        mp['C']=100;
        mp['D']=500;
        mp['M']=1000;
        int sum=0;
        for(int i=0;i<s.length();i++){
            if(i>0&&mp[s[i]]-mp[s[i-1]]>0){
                sum+=mp[s[i]]-2*mp[s[i-1]];
            }else{
                sum+=mp[s[i]];
            }
        }
        return sum;
    }
};
```

# analysis
>虽然想到了map函数，但是不知道罗马数字的规则，还是做不出来，好吧。

## reference
[[编程题]roman-to-integer][1]

[1]: https://www.nowcoder.com/questionTerminal/817fdd12bd3341349a0079f74e692ebf
