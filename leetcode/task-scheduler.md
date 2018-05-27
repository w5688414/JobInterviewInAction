# problem
>Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.
Example 1:
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
```
Note:
1. The number of tasks is in the range [1, 10000].
2. The integer n is in the range [0, 100].

# codes
```
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char,int> mp;
        int count=0;
        for(auto ch:tasks){
            mp[ch]++;
            count=max(count,mp[ch]);
        }
        int ans=(count-1)*(n+1);
        for(auto e:mp){
            if(e.second==count){
                ans++;
            }
        }
        return max((int)tasks.size(),ans);
    }
};
```

# analysis
>能做对这道题的人，估计对操作系统调度原理很熟。我觉得，不然不会想到这种计算方法。
- 由于题目中规定了两个相同任务之间至少隔n个时间点，那么我们首先应该处理的出现次数最多的那个任务，先确定好这些高频任务，然后再来安排那些低频任务。如果任务F的出现频率最高，为k次，那么我们用n个空位将每两个F分隔开，然后我们按顺序加入其他低频的任务，来看一个例子：
AAAABBBEEFFGG 3
我们发现任务A出现了4次，频率最高，于是我们在每个A中间加入3个空位，如下：
A---A---A---A
AB--AB--AB--A   (加入B)
ABE-ABE-AB--A   (加入E)
ABEFABE-ABF-A   (加入F，每次尽可能填满或者是均匀填充)
ABEFABEGABFGA   (加入G)

- 再看一个例子：
ACCCEEE 2
我们发现任务C和E都出现了三次，那么我们就将CE看作一个整体，在中间加入一个位置即可：
CE-CE-CE
CEACE-CE   (加入A)
注意最后面那个idle不能省略，不然就不满足相同两个任务之间要隔2个时间点了。

最后，我们可以找出规律。都被分成了max(x)-1块，max(x)为最大出现次数。比如例子1中，A出现了4次，所以有A---模块出现了3次，再加上最后的A，每个模块的长度为4；例子2中，CE-出现了2次，再加上最后的CE，每个模块长度为3；模块的次数为任务最大次数减1，模块的长度为n+1，最后加上的字母个数为出现次数最多的任务，可能有多个并列。

# reference
[621. Task Scheduler][1]
[[LeetCode] Task Scheduler 任务行程表][2]

[1]: https://leetcode.com/problems/task-scheduler/discuss/104504/C++-8lines-O(n)
[2]: https://www.cnblogs.com/grandyang/p/7098764.html


