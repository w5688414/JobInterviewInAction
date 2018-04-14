# problem
> Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree{1,#,2,3},
```
   1
    \
     2
    /
   3
```
return[1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?



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
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> result;
        if(root==NULL){
            return result;
        }
        stack<TreeNode *> s1;
        TreeNode *temp=root;
        while(!s1.empty()||temp!=NULL){
            while(temp){
                s1.push(temp);
                temp=temp->left;
            }
            
            if(!s1.empty()){
                temp=s1.top();
                s1.pop();
                result.push_back(temp->val);
                temp=temp->right;
            }
        }
        return result;
    }
};

```

# analysis
>用了栈来模拟递归的调用，但是自己写起来，还是不那么顺手。可能还需要练习。

# reference
[[编程题]binary-tree-inorder-traversal][1]

[1]: https://www.nowcoder.com/questionTerminal/1b25a41f25f241228abd7eb9b768ab9b
