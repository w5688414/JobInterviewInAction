# problem
>Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

# codes
```
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res={0};
        for(int i=1;i<=num;i++){
            if(i%2==0){
                res.push_back(res[i/2]);
            }else{
                res.push_back(res[i/2]+1);
            }
        }
        return res;
    }
};
```

# analysis
>这道题目不允许我们用硬办法算答案，那就需要找规律，我也没有想到有这么简洁的解法，规律是，从1开始，遇到偶数时，其1的个数和该偶数除以2得到的数字的1的个数相同，遇到奇数时，其1的个数等于该奇数除以2得到的数字的1的个数再加1。
```
0    0000    0
1    0001    1
2    0010    1
3    0011    2
4    0100    1
5    0101    2
6    0110    2
7    0111    3
8    1000    1
9    1001    2
10   1010    2
11   1011    3
12   1100    2
13   1101    3
14   1110    3
15   1111    4
```

# reference

[[LeetCode] Counting Bits 计数位][1]


[1]: https://www.cnblogs.com/grandyang/p/5294255.html