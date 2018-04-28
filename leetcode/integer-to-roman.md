# problem
>Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

# codes
```
class Solution {
public:
    string intToRoman(int num) {
        string result;
        vector<int> key={1000,900,500,400,100,90,50,40,10,9,5,4,1};
        vector<string> value={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        for(int i=0;i<key.size();i++){
            int count=num/key[i];
            for(int j=0;j<count;j++){
                result+=value[i];
            }
            num=num%key[i];
        }
        return result;
    }
};
```

# analysis
>

| 子母 | M | D | C | L | X | V | I |
| - | :-: | -: | - | :-: | -: |:-: | -:|
| 代表数字 | 1000| 500 | 100 | 50 | 10 | 5 | 1|


# reference
[[编程题]integer-to-roman][1]
[leetcode 罗马数字与整数的转换算法][2]

[1]: https://www.nowcoder.com/questionTerminal/0636c3db0de6437a8a86e58f46aa5c90
[2]: https://blog.csdn.net/net_wolf_007/article/details/51770112