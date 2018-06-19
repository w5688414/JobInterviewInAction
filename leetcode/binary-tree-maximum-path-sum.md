# problem
> Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,
```
       1
      / \
     2   3
```
Return6.

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
private:
    int max_value=INT_MIN;
public:
    int maxPathSum(TreeNode *root) {
        preorder(root);
        return max_value;
    }
    int preorder(TreeNode *root){
        if(root==NULL)
            return 0;
        int left=max(0,preorder(root->left));
        int right=max(0,preorder(root->right));
        max_value=max(max_value,left+right+root->val);
        return max(left,right)+root->val;
    }
};
```

# analysis
>这虽然是一个二叉树遍历的过程，但是结点的值可能为负数，这样我们在计算最大路径值的时候，要注意把求和为负值的分支舍去，保留返回为正值的分支。

# reference
[[编程题]binary-tree-maximum-path-sum][1]

[1]: https://www.nowcoder.com/questionTerminal/da785ea0f64b442488c125b441a4ba4a
