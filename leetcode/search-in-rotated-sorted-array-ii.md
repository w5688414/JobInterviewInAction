# problem
>Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

# codes
```
class Solution {
public:
    bool search(int A[], int n, int target) {
        int left=0;
        int right=n-1;
        while(left<=right){
            int mid=(left+right)/2;
            if(A[mid]==target){
                return true;
            }
            if(A[left]==A[mid]&&A[mid]==A[right]){
                left++;
                right--;
            }
            else if(A[mid]<=A[right]){
                if(A[mid]<target&&A[right]>=target){
                    left=mid+1;
                }else{
                    right=mid-1;
                }
            }else{
                if(A[left]<=target&&A[mid]>target){
                    right=mid-1;
                }else{
                    left=mid+1;
                }
            }
        }
        return false;
    }
};
```

# analysis
>如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的,我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内,这样就可以确定保留哪半边了.
> 这里注意到，left，right，mid的值可能都一样，所以我们需要进一步来缩小范围，很简单,left++,right--就行了。

# reference
[[编程题]search-in-rotated-sorted-array-ii][1]
[[LeetCode] Search in Rotated Sorted Array 在旋转有序数组中搜索][2]

[1]: https://www.nowcoder.com/practice/d942d1aabf5549b0b53af55f1d4432e4?tpId=46&tqId=29097&rp=4&ru=/ta/leetcode&qru=/ta/leetcode/question-ranking
[2]: https://www.cnblogs.com/grandyang/p/4325648.html