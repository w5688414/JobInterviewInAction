# problem
>Given preorder and inorder traversal of a tree, construct the binary tree.

Note: 
You may assume that duplicates do not exist in the tree.

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
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return create(preorder,inorder,0,preorder.size()-1,0,inorder.size()-1);
    }
    
    TreeNode *create(vector<int> &preorder, vector<int> &inorder,int pre_start,int pre_end,int in_start,int in_end) {
        if(pre_start>pre_end){
            return NULL;
        }
        TreeNode *root=new TreeNode(preorder[pre_start]);
        int count=0;
        for(int i=in_start;i<=in_end;i++){
            if(root->val==inorder[i]){
                break;
            }
            count++;
        }
        root->left=create(preorder,inorder,pre_start+1,pre_start+count,in_start,in_start+count-1);
        root->right=create(preorder,inorder,pre_start+count+1,pre_end,in_start+count+1,in_end);
        return root;
    }
};
```

# analysis
>题目的意思是利用前序和中序遍历，本来是跟上一题是差不多的，但是在递归的时候分左右分支索引的时候遇见了点麻烦，之后改变利用count计数找到左右分支，方便了很多。

# reference
[[编程题]construct-binary-tree-from-preorder-and-inorder-traversal][1]

[1]: https://www.nowcoder.com/questionTerminal/0ee054a8767c4a6c96ddab65e08688f4