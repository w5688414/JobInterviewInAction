# problem
>Invert a binary tree.
Example:
Input:
```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```
Output:
```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
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
    TreeNode* invertTree(TreeNode* root) {
        if(!root){
            return NULL;
        }else{
            TreeNode* left=invertTree(root->left);
            TreeNode* right=invertTree(root->right);
            root->left=right;
            root->right=left;
        }
        return root;
    }
};
```

# analysis
>可能自己的递归水平不怎么够，所以这一题我自己没有做出来，看了一下答案，感觉还是蛮简单的，看来还需要多多历练。

# reference
[226. Invert Binary Tree][1]

[1]:https://leetcode.com/problems/invert-binary-tree/solution/
