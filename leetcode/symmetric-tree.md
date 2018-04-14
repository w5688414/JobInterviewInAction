# problem
>Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
But the following is not:
```
    1
   / \
  2   2
   \   \
   3    3
```
Note: 
Bonus points if you could solve it both recursively and iteratively.

confused what"{1,#,2,3}"means? > read more on how binary tree is serialized on OJ.


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


