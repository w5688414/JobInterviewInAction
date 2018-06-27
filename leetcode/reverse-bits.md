# problem
> Reverse bits of a given 32 bits unsigned integer.
Example:
```
Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
```
Follow up:
If this function is called many times, how would you optimize it?

# codes
```
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res=0;
        for(int i=0;i<32;i++){
            if(n&1==1){
                res=(res<<1)+1;
            }else{
                res=res<<1;
            }
            n=n>>1;
        }
        return res;
    }
};
```

# analysis
>没什么说的，深度优先搜索。

# reference
[[LeetCode] Reverse Bits 翻转位][1]

[1]: http://www.cnblogs.com/grandyang/p/4321355.html