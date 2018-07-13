# problem
>Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# codes

## 解法一
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode *sortedListToBST(ListNode *head) {
        return BST(head,NULL);
    }
    TreeNode *BST(ListNode *head,ListNode *tail){
        if(head==tail){
           return NULL;
        }
        ListNode *slow=head;
        ListNode *fast=head;
        while(fast!=tail&&fast->next!=tail){
            slow=slow->next;
            fast=fast->next->next;
        }
        TreeNode *root=new TreeNode(slow->val);
        root->left=BST(head,slow);
        root->right=BST(slow->next,tail);
        return root;
    }
};
```
## s2
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        if(!head){
            return NULL;
        }
        if(!head->next){
            return new TreeNode(head->val);
        }
        ListNode* slow=head;
        ListNode* fast=head;
        ListNode* last=slow;
        while(fast->next&&fast->next->next){
            fast=fast->next->next;
            last=slow;
            slow=slow->next;
        }
        fast=slow->next;
        last->next=NULL;
        TreeNode* root=new TreeNode(slow->val);
        if(head!=slow){
            root->left=sortedListToBST(head);
        }
        root->right=sortedListToBST(fast);
        return root;
    }
};
```

# analysis
>这个思想还不错，很好的利用了快慢指针和递归，快慢指针负责每次找根结点，然后建立根结点，递归负责建树，很巧妙。
## s2
第二个办法算是暴力破解了，也实现了。找到中点后，要以中点的值建立一个数的根节点，然后需要把原链表断开，分为前后两个链表，都不能包含原中节点，然后再分别对这两个链表递归调用原函数，分别连上左右子节点即可。

# reference

[[编程题]convert-sorted-list-to-binary-search-tree][1]

[1]: https://www.nowcoder.com/questionTerminal/86343165c18a4069ab0ab30c32b1afd0