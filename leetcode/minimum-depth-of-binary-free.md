# problem
>Given a binary tree, find its minimum depth.The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# codes
```
class Solution {
public:
    int run(TreeNode *root) {
        if(root==NULL)
            return 0;
        int left=run(root->left);
        int right=run(root->right);
        if(left==0||right==0)
            return left+right+1;
        return 1+min(left,right);
    }
};

```

# analysis
>用了递归，终止条件是root为空，然后取返回值中最小的深度+1，返回到根结点，对于其中一个叶子结点都为空的情况，返回1就行了。
# reference
[[编程题]minimum-depth-of-binary-tree][1]

[1]: https://www.nowcoder.com/questionTerminal/e08819cfdeb34985a8de9c4e6562e724