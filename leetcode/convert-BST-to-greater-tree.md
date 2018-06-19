# problem
>Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
Example:
```
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
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
int sum=0;
public:
    TreeNode* convertBST(TreeNode* root) {
        DFS(root);
        return root;
    }
    
    void DFS(TreeNode* root){
        if(!root){
            return;
        }
        DFS(root->right);
        root->val=sum+root->val;
        sum=root->val;
        DFS(root->left);
    }
};
```

# analysis
>现在对于递归，我能写出一些核心东西，但是不能完整的写出来，可能是自己还没有吃透，还需要继续加油。

# reference
[【LeetCode】538. Convert BST to Greater Tree][1]

[1]: https://blog.csdn.net/mrbcy/article/details/64440395