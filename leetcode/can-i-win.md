# problem
>In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example
```
Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

```

# codes
```
class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if(maxChoosableInteger>desiredTotal){
            return true;
        }
        int sum=maxChoosableInteger*(maxChoosableInteger+1)/2;
        if(sum<desiredTotal){
            return false;
        }
        unordered_map<int,bool> mp;
        return canWin(maxChoosableInteger,desiredTotal,0,mp);
    }
    
    bool canWin(int length,int total,int used,unordered_map<int, bool>& mp){
        if(mp.count(used)) return mp[used];
        for(int i=0;i<length;i++){
            int cur=(1<<i);
            if((cur&used)==0){
                if(total<=i+1||!canWin(length,total-(i+1),cur|used,mp)){
                    mp[used]=true;
                    return true;
                }
            }
        }
        mp[used]=false;
        return false;
    }
};
```

# analysis
>还不怎么懂，明天再看，怕猝死。

# reference
[[LeetCode] Can I Win 我能赢吗][1]
[464. Can I Win][2]


[1]: https://www.cnblogs.com/grandyang/p/6103525.html
[2]: https://leetcode.com/problems/can-i-win/discuss/95278/Java-20-lines-beats-88.8-using-dp-and-backtracking-easy-to-understand!!
