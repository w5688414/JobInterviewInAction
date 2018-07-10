# problem
>Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given1->4->3->2->5->2and x = 3,
return1->2->2->4->3->5.

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
    ListNode *partition(ListNode *head, int x) {
        if(head==NULL){
            return NULL;
        }
       ListNode *dummy = new ListNode(0);
       dummy->next=head;
        ListNode *fast = dummy;
        ListNode *slow = dummy;
        while(fast&&fast->next){
            if(fast->next->val>=x){
                fast=fast->next;
            }else{
                if(fast==slow){
                    fast=fast->next;
                    slow=slow->next;
                }else{
                    ListNode *temp = fast->next;
                    fast->next=temp->next;
                    temp->next=slow->next;
                    slow->next=temp;
                    slow=slow->next;
                }
            }
        }
       return dummy->next;
    }
};

```

# analysis
>原来只需要遍历一遍就行了，slow指针指向要插向的位置，fast来寻找需要移动的结点。

# reference
[[编程题]partition-list][1]

[1]: https://www.nowcoder.com/questionTerminal/1dc1036be38f45f19000e48abe00b12f