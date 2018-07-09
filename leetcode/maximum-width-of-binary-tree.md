# problem
>Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
```
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```
Example 1:
```
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```
Example 2:
```
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
```
Example 3:
```
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
```
Example 4:
```
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
```
Note: Answer will in the range of 32-bit signed integer.

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
    int widthOfBinaryTree(TreeNode* root) {
        int res=0;
        vector<int> start;
        solve(root,0,1,start,res);
        return res;
    }
    void solve(TreeNode* root,int h,int idx,vector<int>& start,int& res){
        if(!root){
            return ;
        }
        if(h>=start.size()) start.push_back(idx);
        res=max(res,idx-start[h]+1);
        solve(root->left,h+1,idx*2,start,res);
        solve(root->right,h+1,idx*2+1,start,res);
    }
};
```

# analysis
>好吧，这个递归我不会写。没想到通过idx计算宽度，start数组存每一行开始元素的下标。


# reference
[[LeetCode] Maximum Width of Binary Tree 二叉树的最大宽度][1]


[1]: http://www.cnblogs.com/grandyang/p/7538821.html