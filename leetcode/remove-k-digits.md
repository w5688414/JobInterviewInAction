# problem
>Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:
```
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```
Example 2:
```
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
```
Example 3:
```
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
```

# codes
```
class Solution {
public:
    string removeKdigits(string num, int k) {
        string res;
        int n=num.size();
        int keep=n-k;
        for(char c:num){
            while(k&&res.size()&&res.back()>c){ //core 
                res.pop_back();
                k--;
            }
            res.push_back(c);
        }
        res.resize(keep);
        while(!res.empty()&&res[0]=='0'){
            res.erase(res.begin());
        }
        return res.empty() ? "0":res;
    }
};
```

# analysis
- 我们用res存储结果，这里有一个规律只要前一个数大于后一个数，删除前一个数，保留后一个数，然后循环删除k个，剩下的就是最小的数。
我并不知道这个规律，没法做。


# reference
[[LeetCode] Remove K Digits 去掉K位数字][1]

[1]: http://www.cnblogs.com/grandyang/p/5883736.html