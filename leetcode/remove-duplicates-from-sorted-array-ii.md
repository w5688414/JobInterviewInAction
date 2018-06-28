# problem
> Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A =[1,1,1,2,2,3],

Your function should return length =5, and A is now[1,1,2,2,3].


# codes

## s1
```
class Solution {
public:
    int removeDuplicates(int A[], int n) {
        int sum=0;
        if(n<=2){
            return n;
        }
        int k=2;
        for(int i=2;i<n;i++){
            if(A[i]!=A[k-2]){
                A[k++]=A[i];
            }
        }
        return k;
    }
};
```
## s2
```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int m=nums.size();
        if(m<=2){
            return m;
        }
        int pre=0;
        int cur=1;
        int count=1;
        while(cur<m){
            if(nums[cur]==nums[pre]&&count==0){
                cur++;
            }else{
                if(nums[cur]==nums[pre]){
                    count--;
                }else{
                    count=1;
                }
                pre++;
                nums[pre]=nums[cur];
                cur++;
            }
        }
       return pre+1;
    }
};
```

# analysis
> 这应该和快慢指针一个道理，索引k为满的满足要求的最后一个值，i遍历原来的串，只要符合要求，那么就可以赋给A的第k个位置，然后k++,i++
## s2
这里允许最多重复的次数是两次，那么我们就需要用一个变量count来记录还允许有几次重复，count初始化为1，如果出现过一次重复，则count递减1，那么下次再出现重复，快指针直接前进一步，如果这时候不是重复的，则count恢复1，由于整个数组是有序的，所以一旦出现不重复的数，则一定比这个数大，此数之后不会再有重复项。

# reference
[[编程题]remove-duplicates-from-sorted-array-ii][1]
[[LeetCode] Remove Duplicates from Sorted Array II 有序数组中去除重复项之二][2]

[1]: https://www.nowcoder.com/questionTerminal/567f420f12ed4069b7e1d1520719d409
[2]: http://www.cnblogs.com/grandyang/p/4329295.html