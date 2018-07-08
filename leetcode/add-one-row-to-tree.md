# problem
>Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.
Example 1:
```
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

```
Example 2:
```
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1

d = 3

Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
```
Note:
1. The given d is in range [1, maximum depth of the given tree + 1].
2. The given binary tree has at least one tree node.

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
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
       if(d==0||d==1){
           TreeNode* newNode=new TreeNode(v);
           (d ? newNode->left:newNode->right)=root;
           return newNode;
       }
        if(root&&d>1){
            root->left=addOneRow(root->left,v,d>2 ? d-1:1);
            root->right=addOneRow(root->right,v, d>2 ? d-1:0);
        }
        return root;
    }
   
};
```

# analysis
>这个递归写法我也没有写出来。
d=0, d=1居然有标记的作用，这倒让我大开眼界，我也做不出来。

# reference
[[LeetCode] Add One Row to Tree 二叉树中增加一行][1]

[1]: http://www.cnblogs.com/grandyang/p/7070182.html