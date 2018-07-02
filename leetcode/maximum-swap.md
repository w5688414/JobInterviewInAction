# problem
>Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
Example 1:
```
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
```
Example 2:
```
Input: 9973
Output: 9973
Explanation: No swap.
```
Note:
1. The given number is in the range [0, 108]

# codes
```
class Solution {
public:
    int maximumSwap(int num) {
        string str=to_string(num);
        int res=num;
        for(int i=0;i<str.size();i++){
            for(int j=i+1;j<str.size();j++){
                swap(str[i],str[j]);
                res=max(res,stoi(str));
                swap(str[i],str[j]);
            }
        }
        return res;
    }
};
```

# analysis
>我用了最原始的暴力破解的方法，后面还有其他以空间换时间的方法，以后尝试一下。


# reference
[[LeetCode] Maximum Swap 最大置换][1]


[1]: http://www.cnblogs.com/grandyang/p/7583875.html