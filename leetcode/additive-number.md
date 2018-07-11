# problem
> Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
```
Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```
Example 2:
```
Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
```
Follow up:
How would you handle overflow for very large input integers?

# codes
```
class Solution {
public:
    bool isAdditiveNumber(string num) {
        for(int i=1;i<num.size();i++){
            for(int j=i+1;j<num.size();j++){
                string s1=num.substr(0,i);
                string s2=num.substr(i,j-i);
                long long d1=stoll(s1.c_str());
                long long d2=stoll(s2.c_str());
                if((s1.size()>1&&s1[0]=='0')||(s2.size()>1&&s2[0]=='0')){
                    continue;
                }
                long long next=d1+d2;
                string nexts = to_string(next);
                string now=s1+s2+nexts;
                while(now.size()<num.size()){
                    d1=d2;
                    d2=next;
                    next=d1+d2;
                    nexts=to_string(next);
                    now+=nexts;
                }
                if(now==num) return true;
            }
        }
        return false;
    }
    
};
```

# analysis
>这道题是暴力破解的，递归的好像不怎么好弄，我这里今后有时间再尝试吧。

# reference
[306. Additive Number][1]

[1]: https://leetcode.com/problems/additive-number/discuss/75704/My-Simple-C++-Non-recursion-Solution