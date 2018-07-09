# problem
>Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
```
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
```
Example 2:
```
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
```

# codes

## s1
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
    bool findTarget(TreeNode* root, int k) {
        if(!root) return false;
        unordered_set<int> s;
        return solve(root,k,s);
    }
    bool solve(TreeNode* root, int k,unordered_set<int> &s){
        if(!root){
            return false;
        }
        if(s.count(k-root->val)){
            return true; 
        }
        s.insert(root->val);
        return solve(root->left,k,s)||solve(root->right,k,s);
    }
};
```


# analysis
>我没做出来，可能是two sum没有学好，好吧，我服。

# reference
[[LeetCode] Two Sum IV - Input is a BST 两数之和之四 - 输入是二叉搜索树][1]


[1]: http://www.cnblogs.com/grandyang/p/7508169.html