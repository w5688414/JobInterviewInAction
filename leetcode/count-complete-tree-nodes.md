# problem
>Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:
```
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
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
    int countNodes(TreeNode* root) {
        if(!root){
            return 0;
        }
        int lh=leftHeight(root);
        int rh=rightHeight(root);
        if(lh==rh) return pow(2,lh)-1;
        return countNodes(root->left)+countNodes(root->right)+1;
    }
    int leftHeight(TreeNode* root){
        if(!root){
            return 0;
        }
        return leftHeight(root->left)+1;
    }
    int rightHeight(TreeNode* root){
        if(!root){
            return 0;
        }
        return rightHeight(root->right)+1;
    }
};
```

# analysis
>我开始写了一个递归，由于复杂度过高，没有通过。后面发现只需要向左递归一次，向右递归一次，然后就行了；然后递归就行了。

# reference

[[LeetCode] Count Complete Tree Nodes 求完全二叉树的节点个数][1]

[1]: http://www.cnblogs.com/grandyang/p/4567827.html
