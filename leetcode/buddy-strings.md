# problem
>Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
Example 1:
```
Input: A = "ab", B = "ba"
Output: true
```
Example 2:
```
Input: A = "ab", B = "ab"
Output: false
```
Example 3:
```
Input: A = "aa", B = "aa"
Output: true
```
Example 4:
```
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
```
Example 5:
```
Input: A = "", B = "aa"
Output: false
```

Note:

1. 0 <= A.length <= 20000
2. 0 <= B.length <= 20000
3. A and B consist only of lowercase letters.

# codes
```
class Solution {
public:
    bool buddyStrings(string A, string B) {
        int m=A.length();
        int n=B.length();
        if(m!=n){
            return false;
        }
        int pos=-1;
        bool isSwap=false;
        bool isRepeat=false;
        vector<int> count(26,0);
        for(int i=0;i<m;i++){
            if(A[i]!=B[i]){
                if(pos==-1){
                    pos=i;
                }else if(isSwap||A[pos]!=B[i]||A[i]!=B[pos]){
                    return false;
                }else{
                    isSwap=true;
                }
            }
            if(++count[A[i]-'a']>1) isRepeat=true;
        }
        return isSwap||isRepeat;
    }
    
};
```

# analysis
>我一开始就无从下手，后面看了别人的解法，发现好简单，肯能是自己被dp吓到了吧。好吧，这是字符串的最后一题，要开启新的刷题旅程了。

# reference
[859. Buddy Strings][1]

[1]: https://leetcode.com/problems/buddy-strings/discuss/142512/13-lines-C++