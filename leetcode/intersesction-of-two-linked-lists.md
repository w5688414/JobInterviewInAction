# problem
>Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:
```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```
begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.



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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *l1=headA;
        ListNode *l2=headB;
        while(l1||l2){
            if(l1){
                l1=l1->next;
            }else{
                headB=headB->next;
            }
            if(l2){
                l2=l2->next;
            }else{
                headA=headA->next;
            }
        }
        while(headA!=headB){
            headA=headA->next;
            headB=headB->next;
        }
        return headA;
    }
};
```

# analysis
>这对我来说是一个简单题了，但是我发现了一个比我以前解法还要好的解法，然后我就试着来写一下，发现真是很奇妙的不用在最开始获取链表的长度，然后不用判断链表是否为空，就能解决，我来学习一下。


# reference
[160. Intersection of Two Linked Lists][1]

[1]: https://leetcode.com/problems/intersection-of-two-linked-lists/solution/