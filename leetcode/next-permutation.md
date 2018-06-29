# problem
>Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3→1,3,2
3,2,1→1,2,3
1,1,5→1,5,1


# codes

## s1
```
class Solution {
public:
    void nextPermutation(vector<int> &num) {
        if(num.size()<=1){
            return;
        }
        int i=num.size()-1;
        while(i>0&&num[i]<=num[i-1]){
            i--;
        }
        if(i==0){
            reverse(num.begin(),num.end());
        }else{
            int j=num.size()-1;
            while(num[j]<=num[i-1]){
                j--;
            }
            swap(num[j],num[i-1]);
            reverse(num.begin()+i,num.end());
        }
    }
};

```

## s2
```
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int m=nums.size();
        int i,j;
        for(i=m-2;i>=0;i--){
            if(nums[i+1]>nums[i]){
                for(j=m-1;j>i;j--){
                    if(nums[j]>nums[i]){
                        break;
                    }
                }
                swap(nums[j],nums[i]);
                reverse(nums.begin()+i+1,nums.end());
                return ;
            }
        }
        reverse(nums.begin(),nums.end());
    }
};
```

# analysis
>比如排列是(2,3,6,5,4,1)，求下一个排列的基本步骤是这样：
1) 先从后往前找到第一个不是依次增长的数，记录下位置p。比如例子中的3，对应的位置是1;
2) 接下来分两种情况：
    (1) 如果上面的数字都是依次增长的，那么说明这是最后一个排列，下一个就是第一个，其实把所有数字反转过来即可(比如(6,5,4,3,2,1)下一个是(1,2,3,4,5,6));
    (2) 否则，如果p存在，从p开始往后找，找到下一个数就比p对应的数小的数字，然后两个调换位置，比如例子中的4。调换位置后得到(2,4,6,5,3,1)。最后把p之后的所有数字倒序，比如例子中得到(2,4,1,3,5,6), 这个即是要求的下一个排列。
以上方法中，最坏情况需要扫描数组三次，所以时间复杂度是O(3*n)=O(n)，空间复杂度是O(1)。

## s2
如果给定数组是降序，则说明是全排列的最后一种情况，则下一个排列就是最初始情况
我们再来看下面一个例子，有如下的一个数组

1　　2　　7　　4　　3　　1

下一个排列为：

1　　3　　1　　2　　4　　7

那么是如何得到的呢，我们通过观察原数组可以发现，如果从末尾往前看，数字逐渐变大，到了2时才减小的，然后我们再从后往前找第一个比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可，步骤如下：

1　　2　　7　　4　　3　　1

1　　2　　7　　4　　3　　1

1　　3　　7　　4　　2　　1

1　　3　　1　　2　　4　　7


# reference
[[编程题]next-permutation][1]
[Next Permutation -- LeetCode][2]
[[LeetCode] Next Permutation 下一个排列][3]

[1]: https://www.nowcoder.com/questionTerminal/f0069cfcd42649e3b6b0c759fae8cde6
[2]: https://blog.csdn.net/linhuanmars/article/details/20434115
[3]: http://www.cnblogs.com/grandyang/p/4428207.html
