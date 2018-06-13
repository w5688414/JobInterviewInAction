# problem
>Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example 1:
```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```
Example 2:
```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

# codes
```
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int left=0;
        int right=nums.size()-1;
        while(true){
            int pos=partition(nums,left,right);
            if(pos==k-1){
                return nums[pos];
            }
            if(pos>k-1){
                right=pos-1;
            }
            if(pos<k-1){
                left=pos+1;
            }
        }
    }
    int partition(vector<int>& nums,int left,int right){
        int value=nums[left];
        int l=left+1;
        int r=right;
        while(l<=r){
            if(nums[l]<value&&nums[r]>value){
                swap(nums[l],nums[r]);
                l++;
                r--;
            }
            if(nums[r]<=value){
                r--;
            }
            if(nums[l]>=value){
                l++;
            }
        }
        swap(nums[left],nums[r]);
        return r;
    }
};
```

# analysis
>这道题目实际上可以直接sort一下就行了，不过后面我发现了有人用快速排序居然也能求出来，我们这里用快速排序的降序方法，我觉得还不错，于是就照葫芦画瓢实现了那种方式。每次快排可以确定一个value的位置，如果那个位置正好等于k-1，则我们就找到了第k大的值；如果不是，如果value的位置<k-1,则第k大的值在右边，对右边的无序数组进行一次快排就行；如果value的位置>k-1，则第k大的值在左边，对左边再进行快排序就行了。思想很巧妙。


# reference
[[LeetCode] Kth Largest Element in an Array 数组中第k大的数字][1]

[1]: https://www.cnblogs.com/grandyang/p/4539757.html