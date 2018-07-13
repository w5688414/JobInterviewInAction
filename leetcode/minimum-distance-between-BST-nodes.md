# problem
>Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example:
```
Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
```
Note:

1. The size of the BST will be between 2 and 100.
2. The BST is always valid, each node's value is an integer, and each node's value is different.

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
    int minDiffInBST(TreeNode* root) {
        int res=INT_MAX;
        int pre=-1;
        solve(root,res,pre);
        return res;
    }
    void solve(TreeNode* root,int& res,int& pre){
        if(!root){
            return ;
        }
        solve(root->left,res,pre);
        if(pre!=-1) res=min(res,root->val-pre);
        pre=root->val;
        solve(root->right,res,pre);
    }
};
```

# analysis
>这个方法跟minimum-absolute-difference-in-BST一样，好吧，我又没看懂。

# reference
[[LeetCode] Minimum Distance Between BST Nodes 二叉搜索树中结点的最小距离][1]

[1]: http://www.cnblogs.com/grandyang/p/9062143.html