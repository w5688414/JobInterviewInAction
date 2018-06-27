# problem
>Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
```
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return build(nums,0,nums.size()-1);
    }
    TreeNode* build(vector<int>& nums,int low,int high){
        if(low>high){
            return NULL;
        }
        int mid=(low+high)/2;
        TreeNode* root=new TreeNode(nums[mid]);
        root->left=build(nums,low,mid-1);
        root->right=build(nums,mid+1,high);
        return root;
    }
};
```

# analysis
>如果将二叉搜索树按中序遍历的话，得到的就是一个有序数组了。那么反过来，我们可以得知，根节点应该是有序数组的中间点，从中间点分开为左右两个有序数组，再分别找出其中间点作为原中间点的左右两个子节点。

# reference
[[LeetCode] Convert Sorted Array to Binary Search Tree 将有序数组转为二叉搜索树][1]

[1]: http://www.cnblogs.com/grandyang/p/4295245.html