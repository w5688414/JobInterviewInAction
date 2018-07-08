# problem
> Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note: 
A solution using O(n ) space is pretty straight forward. Could you devise a constant space solution?

confused what"{1,#,2,3}"means? > read more on how binary tree is serialized on OJ.


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
    void recoverTree(TreeNode* root) {
        TreeNode* first=NULL,*second=NULL,*parent=NULL;
        TreeNode* cur=root;
        TreeNode* pre=NULL;
        while(cur){
            if(!cur->left){
                if(parent&&parent->val>cur->val){ //record
                    if(!first) first=parent;
                    second=cur;
                }
                parent=cur;
                cur=cur->right;
            }else{
                pre=cur->left;
                while(pre->right&&pre->right!=cur) pre=pre->right;
                if(!pre->right){
                    pre->right=cur;
                    cur=cur->left;
                }else{
                    pre->right=NULL;
                    if(parent->val>cur->val){  //record
                        if(!first) first=parent;
                        second=cur;
                    }
                    parent=cur;
                    cur=cur->right;
                }
            }
        }
        if(first&&second) swap(first->val,second->val);
    }
};
```

# analysis
>深度优先搜索，中序遍历，如果前一个结点大于后面的一个结点，则把它记录下来，遍历完后再交换。
## s2
这是O(1)的方式，hard难度，我做不出来，除非对二叉树非常熟悉才行。
这里用到了Morris 遍历.

Morris Traversal方法可以做到这两点，与前两种方法的不同在于该方法只需要O(1)空间，而且同样可以在O(n)时间内完成。

要使用O(1)空间进行遍历，最大的难点在于，遍历到子节点的时候怎样重新返回到父节点（假设节点中没有指向父节点的p指针），由于不能用栈作为辅助空间。为了解决这个问题，Morris方法用到了线索二叉树（threaded binary tree）的概念。在Morris方法中不需要为每个节点额外分配指针指向其前驱（predecessor）和后继节点（successor），只需要利用叶子节点中的左右空指针指向某种顺序遍历下的前驱节点或后继节点就可以了。

中序遍历：
1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。

2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。

   a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。

   b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。

3. 重复以上1、2直到当前节点为空。

```
void inorderMorrisTraversal(TreeNode *root) {
    TreeNode *cur = root, *prev = NULL;
    while (cur != NULL)
    {
        if (cur->left == NULL)          // 1.
        {
            printf("%d ", cur->val);
            cur = cur->right;
        }
        else
        {
            // find predecessor
            prev = cur->left;
            while (prev->right != NULL && prev->right != cur)
                prev = prev->right;

            if (prev->right == NULL)   // 2.a)
            {
                prev->right = cur;
                cur = cur->left;
            }
            else                       // 2.b)
            {
                prev->right = NULL;
                printf("%d ", cur->val);
                cur = cur->right;
            }
        }
    }
}
```

# reference
[[编程题]recover-binary-search-tree][1]
[Morris Traversal方法遍历二叉树（非递归，不用栈，O(1)空间）][2]

[1]: https://www.nowcoder.com/questionTerminal/67c7172122b54b748e78eac7b183b5f3
[2]: https://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html