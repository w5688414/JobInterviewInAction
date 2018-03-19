# problem
>给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。

# codes
```
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
    int count=0;
public:
    TreeNode* KthNode(TreeNode* pRoot, int k)
    {
        if(pRoot==NULL)
            return NULL;
        TreeNode *ret;
        if(pRoot->left){
             ret= KthNode(pRoot->left,k);
        }
        if(ret) return ret;
        count++;
        if(k==count)
            return pRoot;
        if(pRoot->right){
            ret=KthNode(pRoot->right,k);
        }
        return ret;
    }
};

```

# analysis
>这里用到了一个全局变量count，采用的是中序遍历，注意用ret指针来判断递归的返回值。
# reference
[[编程题]二叉搜索树的第k个结点][1]
[1]: https://www.nowcoder.com/questionTerminal/ef068f602dde4d28aab2b210e859150a