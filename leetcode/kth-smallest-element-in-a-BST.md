# problem
>Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
Example 1:
```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```
Example 2:
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# codes
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int ans=0;
        int count=0;
        solve(root,count,ans,k);
        return ans;
    }
    void solve(TreeNode* root,int& count,int& ans,int k){
        if(!root){
            return ;
        }
        solve(root->left,count,ans,k);
        count++;
        if(count==k){
            ans=root->val;
        }else if(count>=k){
            return ;
        }
        solve(root->right,count,ans,k);
    }
};
```

# analysis
>这道题目实际上可以直接sort一下就行了，不过后面我发现了有人用快速排序居然也能求出来，我们这里用快速排序的降序方法，我觉得还不错，于是就照葫芦画瓢实现了那种方式。每次快排可以确定一个value的位置，如果那个位置正好等于k-1，则我们就找到了第k大的值；如果不是，如果value的位置<k-1,则第k大的值在右边，对右边的无序数组进行一次快排就行；如果value的位置>k-1，则第k大的值在左边，对左边再进行快排序就行了。思想很巧妙。


# reference
[230. Kth Smallest Element in a BST][1]

[1]: https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/139983/C++-simple-In-order-solution-and-O(h)-solution