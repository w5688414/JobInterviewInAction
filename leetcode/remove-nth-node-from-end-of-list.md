# problem
>Given a linked list, remove the n-th node from the end of list and return its head.
Example:
```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode* pre=new ListNode(-1);
        pre->next=head;
        ListNode* fast=pre;
        while(n>0&&fast){
            fast=fast->next;
            n--;
        }
        if(n>0){
            return NULL;
        }
        ListNode* slow=pre;
        while(fast->next){
            slow=slow->next;
            fast=fast->next;
        }
        slow->next=slow->next->next;
        return pre->next;
    }
};
```

# analysis
- 快慢指针的一个做法，关键是这是我自己写出来的，唉呀妈呀，太有成就感了。
