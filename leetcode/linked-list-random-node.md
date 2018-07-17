# problem
>Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:
```
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
```
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
private:
    ListNode* head;
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head=head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int res=head->val;
        int i=2;
        ListNode* cur=head->next;
        while(cur){
            int j=rand()%i;
            if(j==0) res=cur->val;
            i++;
            cur=cur->next;
        }
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
```

# analysis
>首先考虑k为1的情况，即：给定一个长度很大或者长度未知数据流，限定对每个元素只能访问一次，写出一个随机选择算法，使得所有元素被选中的概率相等。

设当前读取的是第n个元素，采用归纳法分析如下：

1. n = 1 时，只有一个元素，直接返回即可，概率为1。
2. n = 2 时，需要等概率返回前两个元素，显然概率为1/2。可以生成一个0～1之间的随机数p，p < 0.5 时返回第一个，否则返回第二个。
3. n = 3 时，要求每个元素返回的概率为1/3。注意此时前两个元素留下来的概率均为1/2。做法是：生成一个0～1之间的随机数，若<1/3，则返回第三个，否则返回上一步留下的那个。元素1和2留下的概率均为：1/2 * (1 - 1/3) = 1/3，即上一步留下的概率乘以这一步留下（即元素3不留下）的概率。
4. 假设 n = m 时，前n个元素留下的概率均为：1/n = 1/m；
5. 那么 n = m+1 时，生成0～1之间的随机数并判断是否<1/(m+1)，若是则留下元素m+1，否则留下上一步留下的元素。这样一来，元素m+1留下的概率为1/(m+1)，前m个元素留下来的概率均为：1/m * (1 - 1/(m+1)) = 1/(m+1)，也就是1/n。
6. 综上可知，算法成立。

#reference 
[[LeetCode] Linked List Random Node 链表随机节点][1]
[水塘抽样(Reservoir Sampling)问题][2]

[1]: http://www.cnblogs.com/grandyang/p/5759926.html
[2]: https://www.cnblogs.com/strugglion/p/6424874.html