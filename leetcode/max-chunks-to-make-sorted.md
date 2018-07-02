# problem
>Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:
```
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
```
Example 2:
```
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
```
Note:

- arr will have length in range [1, 10].
- arr[i] will be a permutation of [0, 1, ..., arr.length - 1].

# codes

## s1
```
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int res=0;
        int n=arr.size();
        for(int i=0;i<n;i++){
            int cur=arr[i];
            int j=i+1;
            for(;j<=cur;j++){
                cur=max(cur,arr[j]);
                if(cur>=arr.back()){
                    return res+1;
                }
            }
            i=j-1;
            res++;
        }
        return res;
    }
};
```

# analysis
>分析例子1，这是一个倒序的数组，第一个数字是最大的，为4，那么我们想，这个数字4原本是应该位于数组的最后一个位置，所以中间不可能断开成新的块了，要不然数字4就没法跑到末尾去了。分析到这里，我们应该隐约有点感觉了，当前数字所在的块至少要到达坐标为当前数字大小的地方，比如数字4所在的块至少要包括i=4的那个位置。

分析例子2。第一个数字是1，那么当前数字1所在的块至少要到 i=1 的位置，然后我们去 i=1 的位置上看，发现是数字0，并没有超过 i=1 的范围，那么前两个数就可以断开成一个新的块儿。再往后看，i=2 的位置是2，可以单独断开，后面的3和4也可以分别断开。

# reference
[[LeetCode] Max Chunks To Make Sorted 可排序的最大块数][1]

[1]: http://www.cnblogs.com/grandyang/p/8823944.html