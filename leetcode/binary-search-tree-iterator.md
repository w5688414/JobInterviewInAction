# problem
>Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

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
class BSTIterator {
private:
    stack<TreeNode*> s;
public:
    BSTIterator(TreeNode *root) {
        while(root){
            s.push(root);
            root=root->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode* t=s.top();
        s.pop();
        int res=t->val;
        if(t->right){
            t=t->right;
            while(t){
                s.push(t);
                t=t->left;
            }
        }
        return res;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
```

# analysis

题目的意思是：
实现一个二叉搜索树的遍历迭代器，其中要有next(),hasNext()函数，要求时间复杂度为O(1), 空间复杂度为O(h),h为树的高度。

-这道题我不会，结果看别人的解析，用一个栈就能解决，我要哭了。
初始化的时候，把二叉树遍历root->left压入栈中，
next函数的实现：
把栈顶的元素输出，如果出栈的元素有右分支，把t->right,遍历t->left押入栈中。
hasNext()：
判断一下节点是否为空就行了。

如果读者还是不理解，就直接看代码手动模拟吧，栈能够保证遍历按照从小到大输出。

# reference
[[LeetCode] Binary Search Tree Iterator 二叉搜索树迭代器][1]

[1]: http://www.cnblogs.com/grandyang/p/4231455.html