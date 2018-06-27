# problem
> Given a binary tree
```
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set toNULL.

Initially, all next pointers are set toNULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,
```
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
```
After calling your function, the tree should look like:
```
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
```

# codes

## s1
```
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root)
            return;
        TreeLinkNode *p=root,*q;
        while(p->left){
            q=p;
            while(q){
                q->left->next=q->right;
                if(q->next){
                    q->right->next=q->next->left;
                }
                q=q->next;
            }
            p=p->left;
        }
    }
};
```

## s2
```
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root){
            return;
        }
       if(root->left) root->left->next=root->right;
        if(root->right) root->right->next=root->next ? root->next->left:NULL;
        connect(root->left);
        connect(root->right);
    }
};
```

# analysis
>这种方法的好处是，它利用了自己上一层构造好的next指针，代码简洁巧妙。

## s2
这是个递归的解法，应该很好理解，这次我就写了个递归。

# reference
[[编程题]populating-next-right-pointers-in-each-node][1]
[[LeetCode] Populating Next Right Pointers in Each Node 每个节点的右向指针][2]

[1]: https://www.nowcoder.com/questionTerminal/fdbd05d647084fcf9be78444e231998b
[2]: http://www.cnblogs.com/grandyang/p/4288151.html
