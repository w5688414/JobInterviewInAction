# problem
> Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note: 
A solution using O(n ) space is pretty straight forward. Could you devise a constant space solution?

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
private:
    TreeNode *pre,*a,*b;
public:
    void recoverTree(TreeNode *root) {
        pre=NULL;
        a=NULL;
        b=NULL;
        dfs(root);
       swap(a->val,b->val);
    }
    void dfs(TreeNode *root){
        if(!root)
            return;
        dfs(root->left);
        if(pre&&pre->val>root->val){
            if(!a) a=pre;
            b=root;
        }
        pre=root;
        dfs(root->right);
    }
};
```

# analysis
>深度优先搜索，中序遍历，如果前一个结点大于后面的一个结点，则把它记录下来，遍历完后再交换。
# reference
[[编程题]recover-binary-search-tree][1]

[1]: https://www.nowcoder.com/questionTerminal/67c7172122b54b748e78eac7b183b5f3
