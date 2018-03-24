# problem
>Sort a linked list in O(n log n) time using constant space complexity.
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
    ListNode *sortList(ListNode *head) {
        if(head==NULL||head->next==NULL)
            return head;
        ListNode *p=head;
        ListNode *q=head->next;
        while(q&&q->next){
            p=p->next;
            q=q->next->next;
        }

        ListNode *left=sortList(p->next);
        p->next=NULL;
        ListNode *right=sortList(head);
        return mergeSort(left,right);
    }
    ListNode *mergeSort(ListNode *left,ListNode *right){
        ListNode* dummy = new ListNode(0);
        ListNode *p=dummy;
        while(left&&right){
            if(left->val<right->val){
                p->next=left;
                left=left->next;
            }else{
                p->next=right;
                right=right->next;
            }
            p=p->next;
        }
        if(left){
            p->next=left;
        }
        if(right){
            p->next=right;
        }
        return dummy->next;
    }
};

```

# analysis
>找到链表中点，（快慢指针的思路），写出merge函数归并两个链表。
# reference
[[编程题]sort-list][1]

[1]: https://www.nowcoder.com/questionTerminal/d75c232a0405427098a8d1627930bea6
