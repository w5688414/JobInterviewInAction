# problem
>Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree{3,9,20,#,#,15,7},
```
    3
   / \
  9  20
    /  \
   15   7
```
return its zigzag level order traversal as:
```
[
  [3],
  [20,9],
  [15,7]
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
    vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
        vector<vector<int> >  result;
        if(root==NULL)
            return result;
        deque<TreeNode *> q1;
        TreeNode *temp;
        q1.push_back(root);
        int zz=0;
        while(!q1.empty()){
            int len=q1.size();
            vector<int> ans;
            for(int i=0;i<len;i++){
                if(zz%2!=0){
                    temp=q1.front();
                    ans.push_back(temp->val);
                    q1.pop_front();                    
                    if(temp->right){
                        q1.push_back(temp->right);
                    }
                    if(temp->left){
                        q1.push_back(temp->left);
                    }                    
                }else{
                    temp=q1.back();
                    ans.push_back(temp->val);
                    q1.pop_back();
                    if(temp->left){
                        q1.push_front(temp->left);
                    }
                    if(temp->right){
                        q1.push_front(temp->right);
                    }                    
                }
            }
            zz++;
            result.push_back(ans);
        }
        return result;
    }
};
```

# analysis
>

# reference
[[编程题]binary-tree-zigzag-level-order-traversal][1]
[1]: https://www.nowcoder.com/questionTerminal/47e1687126fa461e8a3aff8632aa5559