# problem
>Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
```
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
```
Example 2:
```
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1

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
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        if(!root){
            return NULL;
        }
        if(root->val<L){
            return trimBST(root->right,L,R);
        }
        if(root->val>R){
            return trimBST(root->left,L,R);
        }
        root->left=trimBST(root->left,L,R);
        root->right=trimBST(root->right,L,R);
        return root;
    }
};
```

# analysis
>递归好简洁，就是没写出来，还自己绕了一个很大的圈子。

# reference
[[LeetCode] Trim a Binary Search Tree 修剪一棵二叉搜索树][1]


[1]: http://www.cnblogs.com/grandyang/p/7583185.html