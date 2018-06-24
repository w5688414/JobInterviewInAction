# problem
> There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:
```
Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
```
Example 2:
```
Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
```
Note:
1. 0 <= N <= 10^5
2. String dominoes contains only 'L', 'R' and '.'

# codes
```
class Solution {
public:
    string pushDominoes(string dominoes) {
        dominoes='L'+dominoes+'R';
        string res="";
        int i=0;
        for(int j=1;j<dominoes.length();j++){
            if(dominoes[j]=='.'){
                continue;
            }
            int middle=j-i-1;
            if(i>0) res+=dominoes[i];
            if(dominoes[i]==dominoes[j]){
                res+=string(middle,dominoes[i]);
            }else if(dominoes[i]=='L'&&dominoes[j]=='R'){
                res+=string(middle,'.');
            }else{
                res+=string(middle/2,'R')+string(middle%2,'.')+string(middle/2,'L');
            }
            i=j;
        }
        return res;
    }
};
```

# analysis
>这应该是刚加进来的题目，我现在还没有水平解析这个，等我有水平能看懂这个代码了，我再把这个补上。

# reference
[838. Push Dominoes][1]

[1]: https://leetcode.com/problems/push-dominoes/discuss/132332/C++JavaPython-Two-Pointers

