# problem 1
>Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list:1->2->3->4->5

For k = 2, you should return:2->1->4->3->5

For k = 3, you should return:3->2->1->4->5

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
    ListNode *reverseKGroup(ListNode *head, int k) {
        if(!head){
            return NULL;
        }
        ListNode *p=head;
        for(int i=0;i<k;i++){
            if(!p){
                return head;
            }
            p=p->next;
        }
        ListNode *newHead=reverse(head,p);
        head->next=reverseKGroup(p,k);
        return newHead;
    }
    ListNode *reverse(ListNode *first,ListNode *last){
        ListNode *pre=NULL;
        while(first!=last){
            ListNode *temp=first->next;
            first->next=pre;
            pre=first;
            first=temp;
        }
        return pre;
    }
};
```

# analysis
>我是想到了可以递归的来翻转，但是我写不出来，看来还是差了一点火候。希望未来能好一点吧。

## reference
[[编程题]reverse-nodes-in-k-group][1]

[1]: https://www.nowcoder.com/questionTerminal/b49c3dc907814e9bbfa8437c251b028e

# problem 2
> Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given1->2->3->4, you should return the list as2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

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
    ListNode *swapPairs(ListNode *head) {
        ListNode *p=head;
        for(int i=0;i<2;i++){
            if(!p){
                return head;
            }
            p=p->next;
        }
        ListNode *newHead=reverse(head,p);
        head->next=swapPairs(p);
        return newHead;
    }
    ListNode * reverse(ListNode *first,ListNode *last){
        ListNode *pre=NULL;
        while(first!=last){
            ListNode *temp=first->next;
            first->next=pre;
            pre=first;
            first=temp;
        }
        return pre;
    }
};
```
# analysis
> 这两道题目的解法很相似，我这里把它们放在一起，看代码就知道了。递归+reverse