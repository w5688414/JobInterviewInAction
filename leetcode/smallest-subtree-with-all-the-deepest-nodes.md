# problem
>
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in it's subtree.
Example 1:
```
Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:
We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
```
Note:

- The number of nodes in the tree will be between 1 and 500.
- The values of each node are unique.
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
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
   
        return solve(root).second;
    }
    pair<int,TreeNode*> solve(TreeNode* root){
        if(!root) return {0,root};
        auto l=solve(root->left);
        auto r=solve(root->right);
        if(l.first==r.first) return {1+l.first,root};
        else if(l.first>r.first) return {1+l.first,l.second};
        else return {1+r.first,r.second};
    }
};
```

# analysis
>这个解法是我看得最明白的，用到pair把深度和root回传，佩服。

# reference
[866. Smallest Subtree with all the Deepest Nodes][1]

[1]: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/discuss/147365/DFS-C++-less10-LOC