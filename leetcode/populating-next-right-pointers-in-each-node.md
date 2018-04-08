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

# analysis
>这种方法的好处是，它利用了自己上一层构造好的next指针，代码简洁巧妙。
# reference
[[编程题]populating-next-right-pointers-in-each-node][1]

[1]: https://www.nowcoder.com/questionTerminal/fdbd05d647084fcf9be78444e231998b
