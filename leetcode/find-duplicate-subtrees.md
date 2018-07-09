# problem
>Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.
Example 1:
```
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
```
The following are two duplicate subtrees:
```
      2
     /
    4
```
and
```
    4
```
Therefore, you need to return above trees' root in the form of a list.

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
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        vector<TreeNode*> res;
        unordered_map<string,int> m;
        solve(root,m,res);
        return res;
    }
    string solve(TreeNode* root,unordered_map<string,int>& m,vector<TreeNode*>& res){
        if(!root) return "#";
        string str=to_string(root->val)+","+solve(root->left,m,res)+","+solve(root->right,m,res);
        if(m[str]==1){
            res.push_back(root);
        }
        m[str]++;
        return str;
    }
};
```

# analysis
>用到了后序遍历，还有数组序列化，并且建立序列化跟其出现次数的映射，这样如果我们得到某个结点的序列化字符串，而该字符串正好出现的次数为1，说明之前已经有一个重复树了，我们将当前结点存入结果res，这样保证了多个重复树只会存入一个结点.

# reference
[[LeetCode] Find Duplicate Subtrees 寻找重复树][1]

[1]: http://www.cnblogs.com/grandyang/p/7500082.html