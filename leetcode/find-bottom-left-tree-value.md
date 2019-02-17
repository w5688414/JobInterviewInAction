# problem
>Given a binary tree, find the leftmost value in the last row of the tree.
Example 1:
```
Input:

    2
   / \
  1   3

Output:
1
```
Example 2:
```
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
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
    int findBottomLeftValue(TreeNode* root) {
        int res;
        int mx=0;
        int cnt=1;
        solve(root,mx,cnt,res);
        return res;
    }
    void solve(TreeNode* root,int& mx,int cnt,int& res){
        if(!root){
            return;
        }
        if(cnt>mx){
            mx=cnt;
            res=root->val;
        }   
        solve(root->left,mx,cnt+1,res);
        solve(root->right,mx,cnt+1,res);
    }
};
```

# analysis
- 题目的意思是：求一棵二叉树中最后一行，最左边的叶子结点。

- 树的问题就是递归，然后是先序遍历，由于先序遍历遍历的顺序是根-左-右，所以每一行最左边的结点肯定最先遍历到，那么由于是新一行，那么当前深度肯定比之前的最大深度大，所以我们可以更新最大深度为当前深度，结点值res为当前结点值，这样在遍历到该行其他结点时就不会更新结果res了。


# reference
[[LeetCode] Find Bottom Left Tree Value 寻找最左下树结点的值][1]

[1]: https://www.cnblogs.com/grandyang/p/6405128.html