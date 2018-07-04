# problem
>Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
Example 1:
```
Input: 123
Output: "One Hundred Twenty Three"
```
Example 2:
```
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```
Example 3:
```
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```
Example 4:
```
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

```

# codes

```
class Solution {
public:
    string numberToWords(int num) {
        string res=solve(num%1000);
        vector<string> v1={"Thousand", "Million", "Billion"};
        for(int i=0;i<3;i++){
            num/=1000;
            res= num%1000 ? solve(num%1000)+ " "+v1[i]+" "+ res:res;
        }
        while(res.back()==' ') res.pop_back();
        return res.empty() ? "Zero":res;
    }
    string solve(int num){
        vector<string> v1 = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        vector<string> v2 = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        string res;
        int a=num/100,b=num%100,c=num%10;
        if(b<20){  // teen
            res=v1[b];
        }else{  //ty
            res=v2[b/10]+ (c ? " "+v1[c]:"");
        }
        if(a>0){  //hundred
            res=v1[a]+" Hundred"+(b ? " "+res:"");
        }
        return res;
    }
};
```

# analysis
- 比如一个三位数n，百位数表示为n/100，后两位数一起表示为n%100，十位数表示为n%100/10，个位数表示为n%10;
- 然后我们看后两位数是否小于20，小于的话直接从数组中取出单词，如果大于等于20的话，则分别将十位和个位数字的单词从两个数组中取出来。
- 然后再来处理百位上的数字，还要记得加上Hundred

这道题目我真心不会，hard题目，不会的始终不会，希望未来做到这道题的时候，能够有思路，能够做对80%。

# reference
[[LeetCode] Integer to English Words 整数转为英文单词][1]

[1]: http://www.cnblogs.com/grandyang/p/4772780.html