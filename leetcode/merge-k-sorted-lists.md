# problem
>Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# codes

## solution 1
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
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if(lists.size()==0){
            return NULL;
        }
        int n=lists.size();
        while(n>1){
            int k=(n+1)/2;
            for(int i=0;i<n/2;i++){
                lists[i]=mergetSort(lists[i],lists[i+k]);
            }
            n=k;
        }
        return lists[0];
    }
    ListNode *mergetSort(ListNode *l1,ListNode *l2){
        ListNode *head=new ListNode(-1);
        ListNode *cur=head;
        while(l1&&l2){
            if(l1->val<l2->val){
                cur->next=l1;
                l1=l1->next;
            }else{
                cur->next=l2;
                l2=l2->next;
            }
            cur=cur->next;
        }
        if(l1){
            cur->next=l1;
        }
        if(l2){
            cur->next=l2;
        }
        return head->next;
    }
};
```

## solution 2
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct cmp {
    bool operator () (ListNode *a, ListNode *b) {
        return a->val > b->val;
    }
};

class Solution {
public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        priority_queue<ListNode*,vector<ListNode*>,cmp> q; 
        for(int i=0;i<lists.size();i++){
            if(lists[i]){
                q.push(lists[i]);
            }
        }
        ListNode *temp=NULL;
        ListNode *pre=NULL;
        ListNode *head=NULL;
        while(!q.empty()){
            temp=q.top();
            q.pop();
            if(!pre){
                head=temp;
            }else{
                pre->next=temp;
            }
            pre=temp;
            if(temp->next){
                q.push(temp->next);
            }
        }
        return head;
    }

};
```

# analysis
>第一种方法是归并排序，分治法，把多路归并转换为二路归并。
>第二种方法虽然能想出来，但是这个最小堆很不好弄，像这样写得很简洁的，我觉得很少见。

# reference
[[LeetCode] Merge k Sorted Lists 合并k个有序链表][1]
[23. Merge k Sorted Lists][2]

[1]:https://www.cnblogs.com/grandyang/p/4606710.html
[2]: https://leetcode.com/problems/merge-k-sorted-lists/solution/
