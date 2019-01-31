# problem
>We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

```
Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
```
```
Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```
```
Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
```
Note:

- The binary tree will have at most 100 nodes.
- The value of each node will only be 0 or 1.

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
    TreeNode* pruneTree(TreeNode* root) {
        
        return solve(root) ? root: NULL;
    }
    bool solve(TreeNode* root){
        if(!root) return false;
        bool a1=solve(root->left);
        bool a2=solve(root->right);
        if(!a1) root->left=NULL;
        if(!a2) root->right=NULL;
        return root->val==1||a1||a2;
    }
};
```

# analysis
题目的意思是：把不包含1的子树去除

一看是树的话，就是递归啦，这里的解决方案是用的或运算符，解法还是挺巧妙的。
- 如果遍历到空节点，直接返回false，如果一个节点的左子树返回为0，说明，要么是空节点，要么是节点的值为0，则左子树可以直接置空，否则不剪枝；一个节点的右子树处理跟左子树一样；然后是当前节点的返回值，如果左右子树的返回值有一个为1或者当前的节点的值为1，则都返回1。


# reference
[814. Binary Tree Pruning][1]
[1]: https://leetcode.com/problems/binary-tree-pruning/solution/