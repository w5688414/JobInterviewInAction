# problem
>
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:
```
              5
             / \
            4   5
           / \   \
          1   1   5
```
Output:
```
2
```
Example 2:
```
              1
             / \
            4   5
           / \   \
          4   4   5
```
Output:
```
2
```
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

# code

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
    int longestUnivaluePath(TreeNode* root) {
        if(!root) return 0;
        int res=0;
        solve(root,root,res);
        return res;
    }
    int solve(TreeNode* root,TreeNode* parent,int& res){
        if(!root) return 0;
        int left=solve(root->left,root,res);
        int right=solve(root->right,root,res);
        if(root->left&&root->val==root->left->val){
            left+=1;
        }else{
            left=0;
        }
        if(root->right&&root->val==root->right->val){
            right++;
        }else{
            right=0;
        }
        res=max(res,left+right);
        return max(left,right);
    }
};
```

# analysis
>我们首先对其左右子结点调用递归函数，得到其左右子树的最大相同值路径，下面就要来看当前结点和其左右子结点之间的关系了，如果其左子结点存在且和当前节点值相同，则left自增1，否则left重置0；同理，如果其右子结点存在且和当前节点值相同，则right自增1，否则right重置0。然后用left+right来更新结果res。而调用当前节点值的函数只能返回left和right中的较大值，因为如果还要跟父节点组path，就只能在左右子节点中选一条path，当然选值大的那个.

# reference
[[LeetCode] Longest Univalue Path 最长相同值路径][1]

[1]: http://www.cnblogs.com/grandyang/p/7636259.html


