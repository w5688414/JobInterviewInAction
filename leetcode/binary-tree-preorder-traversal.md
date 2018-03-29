# problem
>Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree{1,#,2,3},


return[1,2,3].

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
    vector<int> preorderTraversal(TreeNode *root) {
        stack<TreeNode*> stack1;
        vector<int> result;
        if(!root)
            return result; 
        stack1.push(root);
        TreeNode *Node=NULL;
        while(!stack1.empty()){
            Node=stack1.top();
            result.push_back(Node->val);
            stack1.pop();
            if(Node->right){
                stack1.push(Node->right);
            }
            if(Node->left){
                stack1.push(Node->left);
            }
        }
        return result;
    }
};

```

# analysis
>还是用栈，我错误的用了队列。没有考虑周全，看上去跟上一题差不多，这次是没遍历一个结点，就把值放进vector中，便利左右孩子的时候，应该先有孩子，然后左孩子，这样栈取出的时候，才是先左后右，这样就是先序遍历。

# reference
[[编程题]binary-tree-preorder-traversal][1]
[1]: https://www.nowcoder.com/questionTerminal/501fb3ca49bb4474bf5fa87274e884b4