# problem
>Given a singly linked list L: L 0→L 1→…→L n-1→L n,
reorder it to: L 0→L n →L 1→L n-1→L 2→L n-2→…

You must do this in-place without altering the nodes' values.

For example,
Given{1,2,3,4}, reorder it to{1,4,2,3}.
# codes
## s1
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
    void reorderList(ListNode *head) {
        stack<ListNode*> stack1;
        if(!head||!head->next||!head->next->next){
            return;
        }
        ListNode* pre=head;
        ListNode* last=head->next;
        while(last&&last->next){
            pre=pre->next;
            last=last->next->next;
        }
        last=pre->next;
        pre->next=NULL;
        pre=head;
        while(last){
            stack1.push(last);
            last=last->next;
        }
        ListNode* newNode;
        while(!stack1.empty()){
            last=stack1.top();
            stack1.pop();
            newNode=pre->next;
            pre->next=last;
            last->next=newNode;
            pre=newNode;
        }
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
class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head||!head->next||!head->next->next){
            return ;
        }
        ListNode* slow=head;
        ListNode* fast=head;
        while(fast->next&&fast->next->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode* mid=slow->next;
        slow->next=NULL;
        ListNode* last=mid;
        ListNode* pre=NULL;
        while(last){
            ListNode* t=last->next;
            last->next=pre;
            pre=last;
            last=t;
        }
        while(pre&&head){
            ListNode* t=head->next;
            head->next=pre;
            pre=pre->next;
            head->next->next=t;
            head=t;
        }
    }
};
```

# analysis
>这一题的一大半都是自己想出来的，先用快慢指针找到中间结点，然后后面用栈进行反转，然后插入到前面的链表中。
## s2
第二种方法是没有用到栈，只是比前一个解法麻烦了一点，不过我觉得自己也需要锻炼一下吧。

# reference
[[编程题]reorder-list][1]

[1]: https://www.nowcoder.com/questionTerminal/3d281dc0b3704347846a110bf561ef6b