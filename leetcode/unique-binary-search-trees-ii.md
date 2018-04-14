# problem
>Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.
```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

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
    vector<TreeNode *> generateTrees(int n) {
        return helper(1,n);
    }
private:
    vector<TreeNode *> helper(int start,int end){
        vector<TreeNode *> subTree;
        if(start>end){
            subTree.push_back(NULL);
            return subTree;
        }
        for(int k=start;k<=end;k++){ //以k为根节点的树，其左子树由[1, k-1]构成， 其右子树由[k+1, n]构成。该原则建树具有唯一性
            vector<TreeNode *> leftSubs=helper(start,k-1);
            vector<TreeNode *> rightSubs=helper(k+1,end);
            //每个左边的子树跟所有右边的子树匹配，而每个右边的子树也要跟所有的左边子树匹配，总共有左右子树数量的乘积种情况
            for(auto left:leftSubs){
                for(auto right:rightSubs){
                    TreeNode* node=new TreeNode(k);
                    node->left=left;
                    node->right=right;
                    subTree.push_back(node);
                }
            }
        }
        return subTree;
    }
};
```

# analysis
>还是用的递归，把所有可能的左子树和右子树建立起来，然后进行左右子树匹配。见代码注释

# reference
[[编程题]unique-binary-search-trees-ii][1]


[1]: https://www.nowcoder.com/questionTerminal/98aaaefacaca44b9b4f2f2bd75780664
