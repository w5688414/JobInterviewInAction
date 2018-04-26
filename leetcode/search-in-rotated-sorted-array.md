# problem
>Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e.,0 1 2 4 5 6 7might become4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

# codes
```
class Solution {
public:
    int search(int A[], int n, int target) {
        int left=0;
        int right=n-1;
        while(left<=right){
            int mid=(left+right)/2;
            if(A[mid]>target){
                if(A[left]<=target||A[right]>A[mid]){
                    right=mid-1;
                }else{
                    left=mid+1;
                }
            }else if(A[mid]<target){
                if(A[right]>=target||A[left]<A[mid]){
                    left=mid+1;
                }else{
                    right=mid-1;
                }
            }else{
                return mid;
            }
        }
        return -1;
    }
};
```

# analysis
>是一个二分搜索，没什么别的，关键是我自己写出来的，把自己都感动死了。

