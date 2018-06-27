# problem
>Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
- Each element in the result should appear as many times as it shows in both arrays.
- The result can be in any order.

Follow up:
- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# codes
```
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        int m=nums1.size();
        int n=nums2.size();
        int i=0;
        int j=0;
        vector<int> res;
        while(i<m&&j<n){
            if(nums1[i]==nums2[j]){
                res.push_back(nums1[i]);
                i++;
                j++;
            }else if(nums1[i]<nums2[j]){
                i++;
            }else{
                j++;
            }
        }
        return res;
    }
};
```

# analysis
>先排序，然后一个一个的比较，这个方法是我想出来的。
当然可以用hash表，统计nums1每个字符的频率，然后统计nums2中每个字符的频率。
然后遍历取频率最小值就行了哈。


# reference
[[LeetCode] Intersection of Two Arrays II 两个数组相交之二][1]

[1]: http://www.cnblogs.com/grandyang/p/5533305.html