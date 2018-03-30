# problem
>Given an array of integers, every element appears three times except for one. Find that single one.

Note: 
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# codes
```
class Solution {
public:
    int singleNumber(int A[], int n) {
        int ones=0; //记录只出现过1次的bits
        int twos=0; //记录只出现过2次的bits
        int threes=0;
        for(int i=0;i<n;i++){
            int t=A[i];
            twos|=ones&t;  //要在更新ones前面更新twos
            ones ^=t;
            threes=ones&twos;  //ones和twos中都为1即出现了3次
            ones &=~threes;  //抹去出现了3次的bits
            twos &=~threes;
        }
        return ones;
    }
};

```

# analysis
>Single Number的本质，就是用一个数记录每个bit出现的次数，如果一个bit出现两次就归0，这种运算采用二进制底下的位操作^是很自然的。Single Number II中，如果能定义三进制底下的某种位操作，也可以达到相同的效果，Single Number II中想要记录每个bit出现的次数，一个数搞不定就加两个数，用ones来记录只出现过一次的bits，用twos来记录只出现过两次的bits，ones&twos实际上就记录了出现过三次的bits，这时候我们来模拟进行出现3次就抵消为0的操作，抹去ones和twos中都为1的bits。

# reference
[[编程题]single-number-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/1097ca585245418ea2efd0e8b4d9eb7a