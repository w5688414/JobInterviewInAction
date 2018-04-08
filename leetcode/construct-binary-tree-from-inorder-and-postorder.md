# problem
>Given inorder and postorder traversal of a tree, construct the binary tree.

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
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        return build(inorder,postorder,0,inorder.size()-1,0,postorder.size()-1);
    }
    TreeNode * build(vector<int> &inorder, vector<int> &postorder,int in_start,int in_end,int po_start,int po_end){
        if(po_start>po_end){
            return NULL;
        }
        TreeNode *root=new TreeNode(postorder[po_end]);
        int mid=0;
        for(int i=in_start;i<=in_end;i++){
            if(inorder[i]==postorder[po_end]){
                mid=i;
                break;
            }
        }
        root->left=build(inorder,postorder,in_start,mid-1,po_start,po_start+mid-in_start-1);  //mid-in_start-1中序遍历 左中右顺序中的左部分的长度
        root->right=build(inorder,postorder,mid+1,in_end,po_end-in_end+mid,po_end-1);//po_end-(in_end-mid) in_end-mid为中序遍历中的右部分的长度，整个式子会得到右部分在后序遍历中的起点。
        return root;
    }
};

```

# analysis
>利用中序遍历和后续遍历来构造二叉树，需要用到递归，当然这写起来有点费力，总有一个过程，跪着也要跪完。

# reference
[[编程题]construct-binary-tree-from-inorder-and-postorder-traversal][1]

[1]: https://www.nowcoder.com/questionTerminal/b0d07d0edc7f495696aecd265d5ef1b9