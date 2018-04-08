# problem
>Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# codes
```
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode *root) {
        if(root==NULL){
            return true;
        }
        if(abs(maxDepth(root->left)-maxDepth(root->right))>1){
            return false;
        }
        return isBalanced(root->left)&& isBalanced(root->right);
    }
    
    int maxDepth(TreeNode *root){
        if(root==NULL){
            return 0;
        }
        return max(maxDepth(root->left),maxDepth(root->right))+1;
    }
};

```
# analysis
> 判断跟结点的左右分支深度差是否大于1，大于1则返回false.然后再递归的判断左右分支的高度差。

# reference
[[编程题]balanced-binary-tree][1]

[1]: https://www.nowcoder.com/questionTerminal/f4523caf0205476985516212047ac8e7