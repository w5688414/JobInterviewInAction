# problem
> You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int carry=0;
        ListNode *head=new ListNode(0);
        ListNode *pre=head;
        while(l1!=NULL||l2!=NULL||carry!=0){
            int a=(l1==NULL ? 0:l1->val);
            int b=(l2==NULL ? 0:l2->val);
            int sum=a+b+carry;
            ListNode *temp=new ListNode(sum%10);
            carry=sum/10;
            pre->next=temp;
            pre=pre->next;
            l1=(l1==NULL ? l1: l1->next);
            l2=(l2==NULL ? l2: l2->next);
        }
        return head->next;
    }
};
```

# analysis
>这道题，不知道什么原因，我没AC出来，然后借鉴了别人的思路，做出来了，首先创建一个head节点，不存储值，然后遍历l1和l2，然后根据加法运算法则来进行运算，注意里面很巧面的处理，把空的结点的值当作0来对待。

# reference
[[编程题]add-two-numbers][1]

[1]: https://www.nowcoder.com/questionTerminal/56f8d422eae04f129c8e5a05299ae275