# problem
> We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
```
Note:

1. The given tree is non-empty.
2. Each node in the tree has unique values 0 <= node.val <= 500.
3. The target node is a node in the tree.
4. 0 <= K <= 1000.

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
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        vector<int> res;
        solve(root,target,K,res);
        return res;
    }
    int solve(TreeNode* root, TreeNode* target,int K, vector<int>& res){
        if(!root){
           return -1; 
        }else if(root->val==target->val){
            subtree_add(root,0,K,res);
            return 1;
        }else{
            int L=solve(root->left,target,K,res);
            int R=solve(root->right,target,K,res);
            if(L!=-1){
                if(L==K) {
                    res.push_back(root->val);
                }
                subtree_add(root->right,L+1,K,res);
                return L+1;
            }else if(R!=-1){
                if(R==K){
                    res.push_back(root->val);
                }
                subtree_add(root->left,R+1,K,res);
                return R+1;
            }else{
                return -1;
            }
        }  
    }
    void subtree_add(TreeNode* root,int dist,int K,vector<int> &res){
        if(!root) return;
        if(dist==K){
            res.push_back(root->val);
        }else{
            subtree_add(root->left,dist+1,K,res);
            subtree_add(root->right,dist+1,K,res);
        }
    }
};
```

# analysis
>这道题我做不出来
如果root==target， 我们把root结点加入到结果集合。
如果target在root的左分支，距离为L+1,那么我们应该需要在右分支上寻找K-L-1距离的结点；
如果target在root的右分支，算法过程相似；
如果target不在root的左右分支，终止算法。
我们用辅助函数subtree_add方法来添加距离为k-dist的结点。
# reference
[863. All Nodes Distance K in Binary Tree][1]

[1]: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solution/