# problem
> Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
```
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
```
Note:
1. The array is only modifiable by the update function.
2. You may assume the number of calls to update and sumRange function is distributed evenly.

# codes
```
class NumArray {
private:
    vector<int> num;
    vector<int> bit;
public:
    NumArray(vector<int> nums) {
        num.resize(nums.size()+1);
        bit.resize(nums.size()+1);
        for(int i=0;i<nums.size();i++){
            update(i,nums[i]);
        }
    }
    
    void update(int i, int val) {
        int diff=val-num[i+1];
        for(int j=i+1;j<num.size();j+=(j&-j)){
            bit[j]+=diff;
        }
        num[i+1]=val;
    }
    
    int sumRange(int i, int j) {
        return getSum(j+1)-getSum(i);
    }
    int getSum(int i){
        int res=0;
        for(int j=i;j>0;j-=(j&-j)){
            res+=bit[j];
        }
        return res;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
```

# analysis
>这是一个树状数组Binary Indexed Tree的题目，我并不懂，来学习一下吧。
所有的奇数位置的数字和原数组对应位置的相同，偶数位置是原数组若干位置之和，假如原数组A(a1, a2, a3, a4 ...)，和其对应的树状数组C(c1, c2, c3, c4 ...)有如下关系：
C1 = A1
C2 = A1 + A2
C3 = A3
C4 = A1 + A2 + A3 + A4
C5 = A5
C6 = A5 + A6
C7 = A7
C8 = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8
...
那么是如何确定某个位置到底是有几个数组成的呢，原来是根据坐标的最低位Low Bit来决定的，所谓的最低位，就是二进制数的最右边的一个1开始，加上后面的0(如果有的话)组成的数字，例如1到8的最低位如下面所示：
坐标          二进制          最低位

1               0001          1

2               0010          2

3               0011          1

4               0100          4

5               0101          1

6               0110          2

7               0111          1

8               1000          8

...

最低位的计算方法有两种，一种是x&(x^(x–1))，另一种是利用补码特性x&-x。


# reference
[[LeetCode] Range Sum Query - Mutable 区域和检索 - 可变][1]


[1]: http://www.cnblogs.com/grandyang/p/4985506.html