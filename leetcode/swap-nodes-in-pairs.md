# problem
>Given a linked list, swap every two adjacent nodes and return its head.
Example:
```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```
Note:

- Your algorithm should use only constant extra space.
- You may not modify the values in the list's nodes, only nodes itself may be changed.

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
    ListNode* swapPairs(ListNode* head) {

        ListNode* dummy=new ListNode(-1);
        dummy->next=head;
        ListNode* pre=dummy;
        while(pre->next&&pre->next->next){
            ListNode *t=pre->next->next;
            pre->next->next=t->next;
            t->next=pre->next;
            pre->next=t;
            pre=t->next;
        }
        return dummy->next;
    }
};
```

# analysis
>这个连接把我弄晕了，好吧。

# reference
[[LeetCode] Swap Nodes in Pairs 成对交换节点][1]

[1]: http://www.cnblogs.com/grandyang/p/4441680.html