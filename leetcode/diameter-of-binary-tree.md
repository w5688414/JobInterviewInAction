# problem
>Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
Example:
Given a binary tree 
```
          1
         / \
        2   3
       / \     
      4   5    
```
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

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
private:
    int res=0;
public:
    int diameterOfBinaryTree(TreeNode* root) {
        maxDepth(root);
        return res;
    }
    int maxDepth(TreeNode* root){
        if(!root){
            return 0;
        }
        int left=maxDepth(root->left);
        int right=maxDepth(root->right);
        res=max(res,left+right);
        return max(left,right)+1;
    }
};
```

# analysis
>这题我也没有解出来，思路是我们在递归的时候，只需要选择选择当前结点分支的最大长度返回就行了，即max(left,right)+1；当然，res就是左右分支的和了。

# reference

[LeetCode 543. Diameter of Binary Tree 解题笔记][1]

[1]: https://blog.csdn.net/zhyh1435589631/article/details/65939602