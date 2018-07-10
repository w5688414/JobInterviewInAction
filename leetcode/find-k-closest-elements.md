# problem
>Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
```
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
```
Example 2:
```
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
```
Note:
1. The value k is positive and will always be smaller than the length of the sorted array.
2. Length of the given array is positive and will not exceed 104
3. Absolute value of elements in the array and x will not exceed 104

# codes
```
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int i=0;
        int j=arr.size()-k;
        while(i<j){
            int mid=i+(j-i)/2;
            if(x-arr[mid]>arr[mid+k]-x){
                i=mid+1;
            }else{
                j=mid;
            }
        }
        return vector<int> (arr.begin()+i,arr.begin()+i+k);
    }
};
```

# analysis
>每次比较的是mid位置和x的距离跟mid+k跟x的距离，以这两者的大小关系来确定二分法折半的方向，最后找到最近距离子数组的起始位置.

# reference
[[LeetCode] Find K Closest Elements 寻找K个最近元素][1]


[1]: http://www.cnblogs.com/grandyang/p/7519466.html