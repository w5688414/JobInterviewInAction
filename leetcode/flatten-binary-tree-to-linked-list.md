# problem
>Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:
```
    1
   / \
  2   5
 / \   \
3   4   6
```
The flattened tree should look like:
```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
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
    void flatten(TreeNode* root) {
        if(!root){
            return ;
        }
        if(root->left) flatten(root->left);
        if(root->right) flatten(root->right);
        TreeNode *temp=root->right;
        root->right=root->left;
        root->left=NULL;
        while(root->right){
            root=root->right;
        }
        root->right=temp;
    }
};
```

# analysis
>首先找到最左子节点，然后回到其父节点，把父结点点和右子结点断开，然后插入左子结点，然后把右子结点重新连接到右子结点上，然后再回到上一个父节点，重复相同的操作。
例如，对于下面的二叉树，上述算法的变换的过程如下：
```
     1
    / \
   2   5
  / \   \
 3   4   6

     1
    / \
   2   5
    \   \
     3   6
      \    
       4

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
```

# reference
[[LeetCode] Flatten Binary Tree to Linked List 将二叉树展开成链表][1]
[1]: https://www.cnblogs.com/grandyang/p/4293853.html
