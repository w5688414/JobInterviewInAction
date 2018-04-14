# problem
> Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A =[1,1,1,2,2,3],

Your function should return length =5, and A is now[1,1,2,2,3].


# codes
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

# analysis
> 这应该和快慢指针一个道理，索引k为满的满足要求的最后一个值，i遍历原来的串，只要符合要求，那么就可以赋给A的第k个位置，然后k++,i++
# reference
[[编程题]remove-duplicates-from-sorted-array-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/567f420f12ed4069b7e1d1520719d409
