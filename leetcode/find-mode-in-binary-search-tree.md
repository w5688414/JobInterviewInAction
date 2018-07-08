# problem
> 
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
```
   1
    \
     2
    /
   2
```
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).


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
    vector<int> findMode(TreeNode* root) {
        vector<int> res;
        int mx=0,cnt=1;
        TreeNode* pre=NULL;
        solve(root,pre,cnt,mx,res);
        return res;
    }
    void solve(TreeNode* root,TreeNode* &pre,int& cnt,int& mx,vector<int>& res){
       if(!root){
           return ;
       }
        solve(root->left,pre,cnt,mx,res);
        if(pre){
            cnt= root->val==pre->val ? cnt+1:1;
         }
         if(cnt>mx){
             res.clear();
             res.push_back(root->val);
             mx=cnt;
         }else if(cnt==mx){
             res.push_back(root->val);
          }
          pre=root;
          solve(root->right,pre,cnt,mx,res);
    }
};
```

# analysis
>其中一种方法是中序遍历，然后map计算词频，然后再遍历一次，然后求出结果。
这里是另一种方法，中序遍历是有序的，所以只要跟前一个节点比较，如果相等，则cnt+1，不等，置1，并且重新进行统计。
- 标准解释：
所谓的众数就是出现最多次的数字，可以有多个，那么这道题比较直接点思路就是利用一个哈希表来记录数字和其出现次数之前的映射，然后维护一个变量mx来记录当前最多的次数值，这样在遍历完树之后，根据这个mx值就能把对应的元素找出来。

# reference
[[LeetCode] Find Mode in Binary Search Tree 找二分搜索数的众数][1]

[1]: http://www.cnblogs.com/grandyang/p/6436150.html