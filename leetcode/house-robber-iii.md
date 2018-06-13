# problem
>The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.
Example 1:
```
     3
    / \
   2   3
    \   \ 
     3   1
```
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
```
     3
    / \
   4   5
  / \   \ 
 1   3   1
```
Maximum amount of money the thief can rob = 4 + 5 = 9.

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
    int rob(TreeNode* root) {
        unordered_map<TreeNode*,int> mp;
        return dfs(root,mp);
    }
    int dfs(TreeNode* root,unordered_map<TreeNode*,int> &mp){
        if(!root){
            return 0;
        }
        if(mp.count(root)){
            return mp[root];
        }
        int val=0;
        if(root->left){
            val+=dfs(root->left->left,mp)+dfs(root->left->right,mp);
        }
        if(root->right){
            val+=dfs(root->right->left,mp)+dfs(root->right->right,mp);
        }
        val=max(val+root->val,dfs(root->left,mp)+dfs(root->right,mp));
        mp[root]=val;
        return val;
    }
};
```

# analysis
- 这道题目虽然是递归，但是我不会写，然后就看了答案，答案为了减少计算，用了记忆化数组，这里用的是hashmap来实现的。

# reference
[[LeetCode] House Robber III 打家劫舍之三][1]

[1]: https://www.cnblogs.com/grandyang/p/5275096.html