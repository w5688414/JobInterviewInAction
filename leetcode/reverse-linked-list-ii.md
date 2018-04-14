# problem
>Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given1->2->3->4->5->NULL, m = 2 and n = 4,

return1->4->3->2->5->NULL.

Note: 
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        ListNode L = ListNode(0);
        L.next=head;
        ListNode *p=&L; 
        ListNode *q=head;
        for(int i=1;i<m;i++){
            p=q;
            q=q->next;
        }
        for(int i=0;i<n-m;i++){
            ListNode *t = q->next;
            q->next=t->next;
            t->next=p->next;
            p->next=t;
        }
        return L.next;
        
    }
};
```

# analysis
>先遍历到m的位置，然后p指向m位置的前面一个结点，把后面的n-m的next指针反转。

## reference
[[编程题]reverse-linked-list-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/b58434e200a648c589ca2063f1faf58c