# problem
>Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

- age[B] <= 0.5 * age[A] + 7
- age[B] > age[A]
- age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:
```
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
```
Example 2:
```
Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
```
Example 3:
```
Input: [20,30,100,110,120]
Output: 
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
```

Notes:
- 1 <= ages.length <= 20000.
- 1 <= ages[i] <= 120.

# codes
```
class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        int a[121]={};
        int res=0;
        for(auto age:ages){
            ++a[age];
        }
        for(int i=15;i<=120;i++){
            for(int j=0.5*i+8;j<=i;j++){
                res+=a[j]*(a[i]-(i==j));
            }
        }
        return res;
    }
   
};
```

# analysis
>这道题我并没有做出来，O(nlog(n))的解法都没有弄出来，可能自己还是停留在暴力破解的阶段，当不work的时候，就无从下笔了。这个O(n)的解法很特别，直接从15开始，小于15就不满足第一个条件了，然后从0.5A+8开始找满足条件的组合，由于是递增的，满足了第二个条件，最后一个条件可以要可以不要，因为需要A>B。

# reference
[825. Friends Of Appropriate Ages][1]
[1]: https://leetcode.com/problems/friends-of-appropriate-ages/discuss/126930/C++-5-lines-O(n)-sliding-sum
