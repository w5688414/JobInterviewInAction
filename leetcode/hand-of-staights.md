# problem
>Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Example 1:
```
Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
```
Example 2:
```
Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
```
Note:
1. 1 <= hand.length <= 10000
2. 0 <= hand[i] <= 10^9
3. 1 <= W <= hand.length

# codes
```
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        int n=hand.size();
        if(n%W!=0) return false;
        map<int,int> m;
        for(int num:hand){
            m[num]++;
        }
        for(auto it:m){
            if(m[it.first]>0){
                for(int i=W-1;i>=0;i--){
                    if((m[it.first+i]-=m[it.first])<0){
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
```

# analysis
>遍历map，每次减去m[it.first]就行了，等于减去W序列中第一个值的count，这个解法很妙，我想不到。

# reference
[846. Hand of Straights][1]

[1]: https://leetcode.com/problems/hand-of-straights/discuss/135598/C++JavaPython-O(MlogM)-Complexity