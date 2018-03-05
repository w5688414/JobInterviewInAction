# problem
>输入一个链表，输出该链表中倒数第k个结点。

# codes
```
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        ListNode* head=pListHead;
        ListNode* last=pListHead;
        
        if(pListHead==NULL){
            return NULL;
        }
        while(k>0&&last){
            last=last->next;
            k--;
        }
        
        if(k>0)
            return NULL;
        if(last==NULL){
            return pListHead;
        }
        while(last->next!=NULL){
            head=head->next;
            last=last->next;
        }
        return head->next;
    }
};

```

# codes
>我的想法是用两个指针，head和last，先让last沿着链表走k步，然后一步一步的一起走，直到last走到链表末尾位置，然后head指向的结点为第k个结点。这是要注意当链表长度小于k或者没有的情况
# reference
[剑指offer：输入一个链表，输出该链表中倒数第k个结点。][1]

[1]: http://blog.csdn.net/u013686654/article/details/73827816