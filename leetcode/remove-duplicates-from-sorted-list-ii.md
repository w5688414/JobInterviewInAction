# problem
>Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given1->2->3->3->4->4->5, return1->2->5.
Given1->1->1->2->3, return2->3.

# codes
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        ListNode *fast=head;
        ListNode *dummy=new ListNode(-1);
        dummy->next=head;
        ListNode *slow=dummy;
        if(head==NULL)
            return NULL;
        while(fast){
            while(fast->next&&fast->val==fast->next->val){
                fast=fast->next;
            }
            if(slow->next!=fast){
                slow->next=fast->next;
                fast=slow->next;
            }else{
                slow=slow->next;
                fast=fast->next;
            }
        }
        return dummy->next;
    }
};

```
```
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode *L = new ListNode(-1);
        L->next = head;
        ListNode *p = L;
        ListNode *q = L->next;
        while(q)
        {
            while(q->next && q->next->val == q->val)
                q = q->next;
            if(p->next != q)
            {
                ListNode *t = q->next;
                q->next = NULL;
                p->next = t;
                q = t;
            }else{
                p = q;
                q = q->next;
            }
        }
        return L->next;       
    }
};
```

# analysis
- 类似于快慢指针，快指针寻找重复的结点，慢指针指向未重复链表的末尾


# reference
[[编程题]remove-duplicates-from-sorted-list-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/71cef9f8b5564579bf7ed93fbe0b2024