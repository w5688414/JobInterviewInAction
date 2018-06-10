# problem
>Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
Example 1:
Given tree s:
```
     3
    / \
   4   5
  / \
 1   2
```
Given tree t:
```
   4 
  / \
 1   2
```
Example 2:
Given tree s:
```
     3
    / \
   4   5
  / \
 1   2
    /
   0
```
Given tree t:
```
   4
  / \
 1   2
```
Return false.

# codes
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
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(!s){
            return false;
        }
        if(isSame(s,t)){
            return true;
        }
        return isSubtree(s->left,t)||isSubtree(s->right,t);
    }
    bool isSame(TreeNode* s, TreeNode* t){
        if(!s&&!t){
            return true;
        }
        if(!s||!t){
            return false;
        }
        if(s->val!=t->val){
            return false;
        }
        return isSame(s->left,t->left)&&isSame(s->right,t->right);
    }
};
```

# analysis
>子树必须是叶结点开始的，中间某个部分的不能算是子树，那么是不是从s的某个节点开始，跟t的所有结构都一样，这个问题就转换成了判断两棵树是否相同，也就是Same Tree的问题了。我们先从s的根节点出发，跟t比较，如果两棵树完全相同，那么返回true，否则就分别对左子结点和右子结点调用递归来判断是否相同，只要一个返回true了，就表示可以找得到。

# reference
[[LeetCode] Subtree of Another Tree 另一个树的子树][1]

[1]: https://www.cnblogs.com/grandyang/p/6828687.html

