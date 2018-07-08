# problem
>Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.

For example,
Given the following binary tree,
```
         1
       /  \
      2    3
     / \    \
    4   5    7
```
After calling your function, the tree should look like:
```
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
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
    void connect(TreeLinkNode *root) {  //O(n)的空间复杂度
        queue<TreeLinkNode *> q1;
        if(root==NULL)
            return;
        q1.push(root);
        TreeLinkNode* last;
        TreeLinkNode* cur;
        while(!q1.empty()){
            int length=q1.size();
            cur=q1.front();
            q1.pop();
            if(cur->left){ //把左结点加入队列
                q1.push(cur->left);
            }
            if(cur->right){  //把右结点加入队列
                q1.push(cur->right);
            }
            for(int i=0;i<length-1;i++){
                last=q1.front();
                q1.pop();
                if(last->left){ //把左结点加入队列
                    q1.push(last->left);
                }
                if(last->right){ //把右结点加入队列
                    q1.push(last->right);
                }
                cur->next=last;
                cur=cur->next;
            }
            cur->next=NULL;
        }
    }
};
```

```
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {   // O(1)的复杂度
public:
    void connect(TreeLinkNode *root) {
       while(root){
           TreeLinkNode dummy(-1),*prev;
           prev=&dummy;
           for(auto p=root;p;p=p->next){
               if(p->left){
                   prev->next=p->left;
                   prev=prev->next;
               }
               if(p->right){
                   prev->next=p->right;
                   prev=prev->next;
               }
           }
           root=dummy.next; // 指向下一层的第一个节点
       }
    }
};
```

# analysis
>大概是以前做过类似的题目，所以现在照葫芦画瓢做出来了。我用了队列做层序遍历，对于每一层，我们用链表的方式将该层每一个结点链接，不过这是O(n)的空间复杂度
> 另一个很巧妙的用了dummy指针，空间复杂度为O(1),dummy的引用给了pre，当pre第一次赋值的时候，相当于给dummy赋值了，dummy.next永远是一层的第一个节点。过程很巧妙。

## reference
[[编程题]populating-next-right-pointers-in-each-node-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/f18bc13a954f4389900b56e545feca6e