# problem
>Given a linked list, return the node where the cycle begins. If there is no cycle, returnnull.

Follow up:
Can you solve it without using extra space?
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
    ListNode *detectCycle(ListNode *head) {
        if(!head)
            return NULL;
        ListNode *pre=head;
        ListNode *last=head;
        while(last&&last->next){
            pre=pre->next;
            last=last->next->next;
            if(last==pre){
                pre=head;
                while(pre!=last){
                    pre=pre->next;
                    last=last->next;
                }
                return pre;
                }
        }
        return NULL;
    }
};
```

# analysis
>这同样是一个快慢指针的题目，先通过快慢指针判断是否有环，如果有环，则两个指针能够相遇，如果相遇，我们则把其中一个指针指向头结点，然后两个指针同时走，直到两个指针相遇，这样就得到了环的开始结点。

X,Y,Z分别为链表起始位置，环开始位置和两指针相遇位置，则根据快指针速度为慢指针速度的两倍，可以得出：
2*(a + b) = a + b + n * (b + c)；即
a=(n - 1) * b + n * c = (n - 1)(b + c) +c

2*(a+b)为快指针走的步数，b+c为环的长度

注意到b+c恰好为环的长度，故可以推出，如将此时两指针分别放在起始位置和相遇位置，并以相同速度前进，当一个指针走完距离a时，另一个指针恰好走出 绕环n-1圈加上c的距离。
故两指针会在环开始位置相遇。

#reference 
[[编程题]linked-list-cycle-ii][1]
[1]: https://www.nowcoder.com/questionTerminal/6e630519bf86480296d0f1c868d425ad