# problem
>Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

- 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
- F.length >= 3;
- and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:
```
Input: "123456579"
Output: [123,456,579]
```
Example 2:
```
Input: "11235813"
Output: [1,1,2,3,5,8,13]
```
Example 3:
```
Input: "112358130"
Output: []
Explanation: The task is impossible.
```
Example 4:
```
Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
```
Example 5:
```
Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
```
Note:

1. 1 <= S.length <= 200
2. S contains only digits.

# codes
```
class Solution {
public:
    vector<int> splitIntoFibonacci(string S) {
        vector<int> res;
        solve(S,0,res);
        return res;
    }
    
    bool solve(string s,int idx,vector<int> &res){
        if(idx==s.size()&&res.size()>=3){
            return true;
        }
        long num=0;
        for(int i=idx;i<s.size();i++){
            if(i!=idx&&s[idx]=='0'){
                return false;
            }
            num=num*10+s[i]-'0';
            if(num>INT_MAX) return false;
            if(res.size()>=2&&res[res.size()-2]+res.back()!=num) continue;
            res.push_back(num);
            if(solve(s,i+1,res)) return true;
            res.pop_back();
        }
        return false;
    }
};
```

# analysis
>这是一个回溯法，但是我不会写，看来我还是太稚嫩了，希望以后能好一点吧。

# reference
[842. Split Array into Fibonacci Sequence][1]

[1]: https://leetcode.com/problems/split-array-into-fibonacci-sequence/discuss/135687/4ms-backtracking-in-C++