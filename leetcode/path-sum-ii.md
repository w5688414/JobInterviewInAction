# problem
>Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree andsum = 22,
```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
```
return
```
[
   [5,4,11,2],
   [5,8,4,5]
]
```
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
    vector<vector<int> > result;
public:
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<int> ans;
        getPath(root,sum,ans);
        return result;
    }
    void getPath(TreeNode *root, int sum,vector<int> &ans){
        if(root==NULL)
            return;
        ans.push_back(root->val);
        if(root->left==NULL&&root->right==NULL&&sum-root->val==0){
            result.push_back(ans);
        }
        getPath(root->left,sum-root->val,ans);
        getPath(root->right,sum-root->val,ans);
        ans.pop_back();
    }
};

```

# analysis
>这里本质上就是一个二叉树的遍历，注意最后判断条件，当左右子树都为空的时候，说明到达了叶子结点，然后判断是否符合题目要求，我用vector来装路径，如果符合，就把这个vector装进结果集合，这样遍历下去，直到把二叉树遍历完为止。

# reference
[[编程题]path-sum-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/840dd2dc4fbd4b2199cd48f2dadf930a