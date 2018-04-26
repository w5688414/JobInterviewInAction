# problem
>Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given[0,1,0,2,1,0,1,3,2,1,2,1], return6.


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
    bool isSymmetric(TreeNode *root) {
        if(root==NULL){
            return true;
        }
        return isEqual(root->left,root->right);
    }
    bool isEqual(TreeNode *left,TreeNode *right){
        if(left==NULL&&right==NULL){
            return true;
        }
        if(left==NULL||right==NULL){
            return false;
        }
        if(left->val!=right->val){
            return false;
        }
        return isEqual(left->left,right->right)&&isEqual(left->right,right->left);
    }
};

```

# analysis
>递归，把递归的逻辑结构理清楚就行了。
# reference
[[编程题]symmetric-tree][1]

[1]: https://www.nowcoder.com/questionTerminal/1b0b7f371eae4204bc4a7570c84c2de1


