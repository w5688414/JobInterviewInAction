# problem
>Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

confused what"{1,#,2,3}"means? > read more on how binary tree is serialized on OJ.

# codes

## solution 1
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
    bool isValidBST(TreeNode *root) {
        return isValidBST(root,NULL,NULL);
    }
    bool isValidBST(TreeNode *root,TreeNode *min,TreeNode *max){
           if(root==NULL)
                return true;
           if(min&&root->val<=min->val){
               return false;
            }
            if(max&&root->val>=max->val){
                return false;
            } 
        return isValidBST(root->left,min,root)&&isValidBST(root->right,root,max);
    }
};

```
## solution 2

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
    bool isValidBST(TreeNode* root) {
        return judge(root,LONG_MIN,LONG_MAX);
    }
    
    bool judge(TreeNode *root, long min_val,long max_val){
        if(root==NULL){
            return true;
        }
        if(root->val<=min_val||root->val>=max_val){
            return false;
        }
        return judge(root->left,min_val,root->val)&&judge(root->right,root->val,max_val);
    }
};
```

# analysis
>对于一棵二叉搜索树，根结点必须比所有的左子树的值大，然后比右子树的所有的值小。这样就很好理解为什么要用min,max指针了。
解法二中要注意数的溢出问题。

# reference
[[编程题]validate-binary-search-tree][1]
[[LeetCode] Validate Binary Search Tree 验证二叉搜索树][2]


[1]: https://www.nowcoder.com/questionTerminal/fd7f880072914464a13b89af242c0ce5
[2]:https://www.cnblogs.com/grandyang/p/4298435.html
