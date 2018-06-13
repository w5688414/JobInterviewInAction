# problem
>Given a singly linked list, determine if it is a palindrome.
Example 1:
```
Input: 1->2
Output: false
```
Example 2:
```
Input: 1->2->2->1
Output: true
```
Follow up:
Could you do it in O(n) time and O(1) space?

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
    bool isPalindrome(ListNode* head) {
        if(!head||!head->next) return true;
        ListNode* slow=head;
        ListNode* fast=head;
        while(fast->next&&fast->next->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode* last=slow->next;
        ListNode* pre=head;
        while(last->next){
            ListNode* temp=last->next;
            last->next=temp->next;
            temp->next=slow->next;
            slow->next=temp;
        }
        last=slow->next;
        while(last){
            if(pre->val!=last->val){
                return false;
            }
            pre=pre->next;
            last=last->next;
        }
        return true;
    }
};
```

# analysis
>很直接的方法就是先找到链表的中点，这可以通过快慢指针获得，然后反转后面的链表。最后分别从中点->next和head出发，挨个的进行比较，这就是上面描述的方法。另一种方法可以用栈空间，在快慢指针寻找中点的过程中，把慢指针遍历的结点压入栈中；找到中点后，我们依次出栈跟后面的链表的值进行比较，可以得到结果，但是这用了栈空间，所以不符合题意。

# reference
[[LeetCode] Palindrome Linked List 回文链表][1]

[1]: https://www.cnblogs.com/grandyang/p/4635425.html
