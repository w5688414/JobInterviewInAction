# problem
> Given a binary tree, return the postorder traversal of its nodes' values.
For example:
Given binary tree{1,#,2,3},
return[3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

# codes

## s1
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
    vector<int> postorderTraversal(TreeNode *root) {
        stack<TreeNode*> stack1;
        vector<int> result;
        if(!root){
            return result;
        }
        stack1.push(root);
        TreeNode* Node=NULL;
        while(!stack1.empty()){
            Node=stack1.top();
            if(Node->left==NULL&&Node->right==NULL){
                result.push_back(Node->val);
                stack1.pop();
            }else{
                if(Node->right){
                    stack1.push(Node->right);
                    Node->right=NULL;
                }
                if(Node->left){
                    stack1.push(Node->left);
                    Node->left=NULL;
                }
            }
           
        }
        return result;
    }
};
```
## s2
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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        if(!root){
            return res;
        }
        stack<TreeNode*> s;
        s.push(root);
        TreeNode* head=root;
        while(!s.empty()){
            TreeNode* t=s.top();
            if((!t->left&&!t->right)||t->left==head||t->right==head){
                res.push_back(t->val);
                s.pop();
                head=t;
            }else{
                if(t->right){
                    s.push(t->right);
                }
                if(t->left){
                    s.push(t->left);
                }
            }
        }
        return res;
    }
};
```

# analysis
>非递归的化，需要用到栈，注意进栈的顺序。如果结点的左右孩子都为空，说明到了叶结点。在遍历左右孩子的时候，我们在加入栈的的同时，要注意置空，不然出栈回溯的时候又会向下遍历
## s2
这份代码我觉得写得不错，毕竟用了head指针，避免了继续递归，而直接返回。和s1的置空的效果一样。
# reference
[[编程题]binary-tree-postorder-traversal][1]

[1]: https://www.nowcoder.com/questionTerminal/32af374b322342b68460e6fd2641dd1b
