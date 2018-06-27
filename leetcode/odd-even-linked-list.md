# problem
>Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
```
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
```
Example 2:
```
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
```
Note:
1. The relative order inside both the even and odd groups should remain as it was in the input.
2. The first node is considered odd, the second node even and so on ...

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
    ListNode* oddEvenList(ListNode* head) {
        if(!head||!head->next){
            return head;
        }
        ListNode* odd=head;
        ListNode* even=head->next;
        ListNode* even_head=even;
        while(even&&even->next){
            odd->next=even->next;
            odd=odd->next;
            even->next=odd->next;
            even=even->next;
        }
        odd->next=even_head;
        return head;
    }
};
```

# analysis
> 这道题目一开始我没有做出来，原因是链表的链接有问题了，还缺了点火候。后面看了别人的，豁然开朗，一下子就写出来了。希望以后自己能独立的写出来。


# reference
[[LeetCode] Odd Even Linked List 奇偶链表][1]

[1]: http://www.cnblogs.com/grandyang/p/5138936.html


