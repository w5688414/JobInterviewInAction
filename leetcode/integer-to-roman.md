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

- 规则

1. 相同的数字连写， 所表示的数等于这些数字相加得到的数。如 XXX表示 30
2. 小的数字在大的数字的右边， 所表示的数等于这些数字相加得到的数 如VIII 表示8
3. 小的数字(限于I, X, C)在大的数字的左边， 所表示的数等于大数减去小的数： 如IV 表示4
4. 在一个数的上面画一条横线， 表示这个数增值1000倍(由于题目只考虑4000以内的数，所以这条规则不用考虑)。

- 五个组数规则
1. I, X, C： 最多只能连用3个， 如果放在大数的左边，只能用1个。
2. V, L, D: 不能放在大数的左边，只能使用一个。
3. I 只能用在V和X的左边。 IV表示4, IX表示9
4. X只能放在L,C左边。 XL 表示40, XC表示90
5. C只能用在D, M左边。 CD 表示400, CM表示900

# reference
[[编程题]integer-to-roman][1]
[leetcode 罗马数字与整数的转换算法][2]
[利用Markdown创建表格][3]

[1]: https://www.nowcoder.com/questionTerminal/0636c3db0de6437a8a86e58f46aa5c90
[2]: https://blog.csdn.net/net_wolf_007/article/details/51770112
[3]: https://blog.csdn.net/tuxingchen6/article/details/55222951