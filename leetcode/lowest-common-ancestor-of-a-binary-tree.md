# problem
>Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary search tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
```
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
```
Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
```
Example 2:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root||p==root||q==root){
            return root;
        }
        TreeNode* left=lowestCommonAncestor(root->left,p,q);
        TreeNode* right=lowestCommonAncestor(root->right,p,q);
        if(left&&right){
            return root;
        }
        return left ? left:right;
    }
};
```

# analysis
>首先要先确定给的两个node是否都在tree里，如果都在tree里的话，就可以分成3种情况，第一种情况是两个节点是在公共祖先的左右两侧，第二种情况是都在树的左侧，第三种情况是都在树的右侧，如果是第二，第三种情况的话，公共祖先就在给定的两个点中比较上面的那一个。


# reference
[[LeetCode] Lowest Common Ancestor of a Binary Tree 二叉树的最小共同父节点][1]
[[LeetCode] Lowest Common Ancestor of a Binary Tree系列][2]

[1]: https://www.cnblogs.com/grandyang/p/4641968.html
[2]: https://segmentfault.com/a/1190000009429876

