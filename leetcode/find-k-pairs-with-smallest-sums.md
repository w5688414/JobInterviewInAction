# problem
>You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
Example 1:
```
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```
Example 2:
```
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```
Example 3:
```
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
```
# codes
```
class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int,int>> res;
        if(nums1.empty()||nums2.empty()){
            return res;
        }
        int n1=nums1.size();
        int n2=nums2.size();
        for(int i=0;i<min(n1,k);i++){
            for(int j=0;j<min(n2,k);j++){
                res.push_back({nums1[i],nums2[j]});
            }
        }
        sort(res.begin(),res.end(),[](pair<int,int> p1,pair<int,int> p2){
            return p1.first+p1.second<p2.first+p2.second;
        });
        k= k<res.size() ? k:res.size(); 
        return vector<pair<int,int>>(res.begin(),res.begin()+k);
    }
};
```

# analysis
>每次比较的是mid位置和x的距离跟mid+k跟x的距离，以这两者的大小关系来确定二分法折半的方向，最后找到最近距离子数组的起始位置.

# reference
[[LeetCode] Find K Pairs with Smallest Sums 找和最小的K对数字][1]


[1]: http://www.cnblogs.com/grandyang/p/5653127.html