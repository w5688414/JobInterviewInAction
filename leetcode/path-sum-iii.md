# problem
>You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
Example:
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

```

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
    int pathSum(TreeNode* root, int sum) {
        if(!root) return 0;
        return getSum(root,0,sum)+pathSum(root->left,sum)+pathSum(root->right,sum);
    }
private:
    int getSum(TreeNode* root, int cur,int sum){
        if(!root){
            return 0;
        }
        cur=cur+root->val;
        return (sum==cur)+getSum(root->left,cur,sum)+getSum(root->right,cur,sum);
    }
};
```

# analysis
>我开始也是想的递归，但是开在以任意根结点出发那里了，原来可以这样做，看来还需要进一步熟悉。

# reference
[437. Path Sum III][1]

[1]: https://leetcode.com/problems/path-sum-iii/discuss/91877/C++-5-Line-Body-Code-DFS-Solution