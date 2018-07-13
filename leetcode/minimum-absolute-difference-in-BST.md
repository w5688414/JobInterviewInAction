# problem
>Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:
```
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
```
Note: There are at least two nodes in this BST.

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
    int getMinimumDifference(TreeNode* root) {
        int res=INT_MAX;
        int pre=-1;
        solve(root,pre,res);
        return res;
    }
    void solve(TreeNode* root,int& pre,int& res){
        if(!root){
            return;
        }
        solve(root->left,pre,res);
        if(pre!=-1) res=min(res,root->val-pre);
        pre=root->val;
        solve(root->right,pre,res);
    }
};
```

# analysis
>这道题我并没有写出来，是中序遍历，卡在了怎么计算上面，看来还需要磨练。


# reference
[[LeetCode] Minimum Absolute Difference in BST 二叉搜索树的最小绝对差][1]

[1]: http://www.cnblogs.com/grandyang/p/6540165.html