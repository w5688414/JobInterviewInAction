# problem
>There are two types of soup: type A and type B. Initially we have N ml of each type of soup. There are four kinds of operations:

- Serve 100 ml of soup A and 0 ml of soup B
- Serve 75 ml of soup A and 25 ml of soup B
- Serve 50 ml of soup A and 50 ml of soup B
- Serve 25 ml of soup A and 75 ml of soup B
When we serve some soup, we give it to someone and we no longer have it.  Each turn, we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.  We stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.  

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.

```
Example:
Input: N = 50
Output: 0.625
Explanation: 
If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
```
Notes:
- 0 <= N <= 10^9. 
- Answers within 10^-6 of the true value will be accepted as correct.

# codes
```
class Solution {
    
public:
    double soupServings(int N) {
        if(N>10000)
            return 1;
        vector<vector<double>> memo(400,vector<double>(400,0.0));
        return solve((N+24)/25,(N+24)/25,memo);
    }
    double solve(int a,int b,vector<vector<double>> &memo){
        if(a<=0&&b<=0){
            return 0.5;
        }
        if(a<=0){
            return 1.0;
        }
        if(b<=0){
            return 0.0;
        }
        if(memo[a][b]>0)
            return memo[a][b];
        memo[a][b]=0.25*(solve(a-4,b,memo)+solve(a-3,b-1,memo)+solve(a-2,b-2,memo)+solve(a-1,b-3,memo));
        return memo[a][b];
    }
};
```

# analysis
>我开始没看懂题目，看见概率的题目，我有点后怕，大概是上次被阿里的题目吓到的缘故。回头发现还是蛮中规中矩的题目，用了记忆化数组进行剪枝。
其实记忆化数组可以变成dp的方法的，这里就先放一放。

# reference
[808-Soup Servings][1]

[1]: https://blog.csdn.net/laputafallen/article/details/79777115