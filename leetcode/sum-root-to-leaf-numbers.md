# problem
>Given a binary tree containing digits from0-9only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path1->2->3which represents the number123.

Find the total sum of all root-to-leaf numbers.

For example,
```
    1
   / \
  2   3
```
The root-to-leaf path1->2represents the number12.
The root-to-leaf path1->3represents the number13.

Return the sum = 12 + 13 =25.

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
    int sumNumbers(TreeNode *root) {
        int sum=0;
        if(root==NULL){
            return sum;
        }
        return preorder(root,sum);
    }
    
    int preorder(TreeNode *root,int sum){
        if(root==NULL){
            return 0;
        }
        sum=sum*10+root->val;
        if(root->left==NULL && root->right==NULL){
            return sum;
        }
        return preorder(root->left,sum)+preorder(root->right,sum);
    }
};

```

# analysis
>先序遍历每个结点，用一个sum变量保存求和的值，每一层都比上层和*10+当前根节点的值。
# reference
[[编程题]sum-root-to-leaf-numbers][1]

[1]: https://www.nowcoder.com/questionTerminal/185a87cd29eb42049132aed873273e83
