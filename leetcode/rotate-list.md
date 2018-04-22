# problem
>Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given1->2->3->4->5->NULLand k =2,
return4->5->1->2->3->NULL.

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
    ListNode *rotateRight(ListNode *head, int k) {
        ListNode *p=head;
        if(head==NULL||k==0){
            return head;
        }
        int len=1;
        while(p->next){ //遍历一遍，求出链表长度
            p=p->next;
            len++;
        }
        k=len-k%len;
        p->next=head; //首尾相连
        for(int i=0;i<k;i++){
            p=p->next;
        }
        head=p->next;
        p->next=NULL; //断开环
        return head;
    
    }
};
```

# analysis
>这里注意k可以大于链表的长度，然后我们可以把链表首位连接，只需要从head走len-k%len步，从那个结点之前的结点断开，head指向那个结点，把前面一个结点的next指针设置为NULL就行了。我开始还是想复杂了，结果总是work不了。

## reference
[[编程题]rotate-list][1]

[1]: https://www.nowcoder.com/questionTerminal/afbec6b9d4564c63b2c149ccc01c5678