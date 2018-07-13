# problem
>GSort a linked list using insertion sort.
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
    ListNode *insertionSortList(ListNode *head) {
        if(head==NULL)
            return head;
        ListNode *p=head;
        ListNode *q=head->next;
        ListNode *temp;
        while(q){
            if(p->val<=q->val){
                p=p->next;
                q=q->next;
            }else if(head->val>q->val){
                p->next=q->next;
                q->next=head;
                head=q;
                q=p->next;
                
            }else{
                temp=head;
                while(temp->next->val<q->val){
                    temp=temp->next;
                }
                p->next=q->next;
                q->next=temp->next;
                temp->next=q;
                q=p->next;
            }
        }
        return head;
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
    ListNode* insertionSortList(ListNode* head) {
        ListNode* dummy=new ListNode(-1);
        ListNode* cur;
        while(head){
            ListNode* t=head->next;
            cur=dummy;
            while(cur->next&&cur->next->val<head->val){
                cur=cur->next;
            }
            head->next=cur->next;
            cur->next=head;
            head=t;
        }
        return dummy->next;
    }
};
```

# analysis
>链表的插入排序我还是第一次做，这里需要分情况讨论，插入到头结点的话，头结点需要变，然后插入到中间某个结点，我们需要遍历找到那个结点的前面和后面的结点，然后插入。
## s2
用了额外变量dummy来实现，相对来说实现起来就简单多了。

# reference
[[编程题]insertion-sort-list][1]

[1]: https://www.nowcoder.com/questionTerminal/152bc6c5b14149e49bf5d8c46f53152b