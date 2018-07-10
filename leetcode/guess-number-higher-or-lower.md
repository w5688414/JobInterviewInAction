# problem
>We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
```
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
```
Example:
```
n = 10, I pick 6.

Return 6.
```

# codes
```
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int i=1;
        int j=n;
        while(i<j){
            int mid=i+(j-i)/2;
            int t=guess(mid);
            if(t==0){
                return mid;
            }else if(t==1){
                i=mid+1;
                
            }else{
                j=mid-1;
            }
        }
        return i;
    }
};
```

# analysis
>这道题我没有理解题意，直接把i和j更新的判断条件写反了，导致晕了好一段时间。

# reference
[[LeetCode] Guess Number Higher or Lower 猜数字大小][1]

[1]: http://www.cnblogs.com/grandyang/p/5666502.html
