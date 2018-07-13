# problem
>Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?
Example:
```
Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
```

# codes
```
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int res=0;
        int mask=0;
         // from left to right
        for(int i=31;i>=0;i--){
            mask|=(1<<i); //11110000
            unordered_set<int> s;
            for(int num:nums){
                s.insert(num&mask);
            }
            int t=res|(1<<i); // t, res: 10101000000, add more 1 
            for(int prefix:s){ // 利用了 ^ 的 a ^ b = c，则 b ^ c = a
                if(s.count(t^prefix)){
                    res=t;
                    break;
                }
            }
        }
        return res;
    }
};
```

# analysis
>这道题我不会，还没搞懂是什么原理。
利用了异或的”自反性“： a ^ b = c，而a ^ b ^ b = a, 则 c ^ b = a
计算使用的结果，不是只看一位，而是每次把新的一位加到原来的结果后面。这样的好处是不需要记录之前的结果满足条件的有哪些，每次就重新计算和查找就可以了，大大降低了复杂度。


# reference
[[LeetCode] Maximum XOR of Two Numbers in an Array 数组中异或值最大的两个数字][1]
[【特别好】【位运算】maximum-xor-of-two-numbers-in-an-array][2]

[1]: http://www.cnblogs.com/grandyang/p/5991530.html
[2]: https://www.cnblogs.com/charlesblc/p/5966368.html