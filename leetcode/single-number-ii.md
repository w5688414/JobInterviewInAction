# problem
>Given an array of integers, every element appears three times except for one. Find that single one.

Note: 
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# codes
## s1
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
## s2
```
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int a=0,b=0;
        for(int i=0;i<nums.size();i++){
            b=(b^nums[i])&~a;
            a=(a^nums[i])&~b;
        }
        return b;
    }
};
```

# analysis
>Single Number的本质，就是用一个数记录每个bit出现的次数，如果一个bit出现两次就归0，这种运算采用二进制底下的位操作^是很自然的。Single Number II中，如果能定义三进制底下的某种位操作，也可以达到相同的效果，Single Number II中想要记录每个bit出现的次数，一个数搞不定就加两个数，用ones来记录只出现过一次的bits，用twos来记录只出现过两次的bits，ones&twos实际上就记录了出现过三次的bits，这时候我们来模拟进行出现3次就抵消为0的操作，抹去ones和twos中都为1的bits。
## s2
没理解的话，果然还是不会做。
我们把数组中数字的每一位累加起来对3取余，剩下的结果就是那个单独数组该位上的数字，由于我们累加的过程都要对3取余，那么每一位上累加的过程就是0->1->2->0，换成二进制的表示为00->01->10->00，那么我们可以写出对应关系：
00 (+) 1 = 01

01 (+) 1 = 10

10 (+) 1 = 00 ( mod 3)
那么我们用ab来表示开始的状态，对于加1操作后，得到的新状态的ab的算法如下：
b = b xor r & ~a;

a = a xor r & ~b;

我们这里的ab就是上面的三种状态00，01，10的十位和个位，刚开始的时候，a和b都是0，当此时遇到数字1的时候，b更新为1，a更新为0，就是01的状态；再次遇到1的时候，b更新为0，a更新为1，就是10的状态；再次遇到1的时候，b更新为0，a更新为0，就是00的状态，相当于重置了；最后的结果保存在b中。
方程我不知道怎么推出来的，神奇，不过验证了结果是正确的。

# reference
[[编程题]single-number-ii][1]
[[LeetCode] Single Number II 单独的数字之二][2]

[1]: https://www.nowcoder.com/questionTerminal/1097ca585245418ea2efd0e8b4d9eb7a
[2]: http://www.cnblogs.com/grandyang/p/4263927.html