# problem
>Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
Example 1:
```
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
```
Example 2:
```
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
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
    int findSecondMinimumValue(TreeNode* root) {
        int first=root->val,second=INT_MAX;
        solve(root,first,second);
        return (first==second||second==INT_MAX) ? -1:second;
    }
    void solve(TreeNode* root,int& first,int& second){
        if(!root){
            return ;
        }
        if(root->val!=first&&root->val<second){
            second=root->val;
        }
        solve(root->left,first,second);
        solve(root->right,first,second);
    }
};
```

# analysis
>根结点一定是最小的结点值first，那么我们只要找出第二小的值second即可，初始化为整型的最大值。然后对根结点调用递归函数，将first和second当作参数传进去即可。在递归函数中，如果当前结点为空，直接返回，若当前结点孩值不等于first，说明其肯定比first要大，然后我们看其是否比second小，小的话就更新second，然后对当前结点的左右子结点分别调用递归函数即可.

这道题我也没有做出来，可能是自己功力不够，或者对题目理解不够透彻。
# reference
[[LeetCode] Second Minimum Node In a Binary Tree 二叉树中第二小的结点][1]

[1]: http://www.cnblogs.com/grandyang/p/7590156.html

