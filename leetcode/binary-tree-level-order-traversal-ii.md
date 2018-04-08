# problem
>Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree{3,9,20,#,#,15,7},
```
    3
   / \
  9  20
    /  \
   15   7
```
return its bottom-up level order traversal as:
```
[
  [15,7]
  [9,20],
  [3],
]
```
confused what"{1,#,2,3}"means? > read more on how binary tree is serialized on OJ.

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
public:
    vector<vector<int> > levelOrderBottom(TreeNode *root) {
        vector<vector<int> > result;
        if(root==NULL)
            return result;
        queue<TreeNode *> q1;
        TreeNode *temp;
        q1.push(root);
        while(!q1.empty()){
            int length=q1.size();
            vector<int>  level;
            for(int i=0;i<length;i++){
                temp=q1.front();
                q1.pop();
                level.push_back(temp->val);
                if(temp->left){
                    q1.push(temp->left);
                }
                if(temp->right){
                    q1.push(temp->right);
                }
            }
            result.push_back(level);
        }
        reverse(result.begin(),result.end());
        return result;
    }
};
```

# analysis
> 这道题目用了BFS，进行层序遍历，用队列来实现这一过程。然后用vector装结果，由于题目要求自底向上，我们是自顶向下求的，因此我们需要把顺序翻转一下。

# reference
[[编程题]binary-tree-level-order-traversal-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/d8566e765c8142b78438c133822b5118
