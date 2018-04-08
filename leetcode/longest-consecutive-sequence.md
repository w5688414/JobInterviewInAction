# problem
>Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given[100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is[1, 2, 3, 4]. Return its length:4.

Your algorithm should run in O(n) complexity.

# codes
```
class Solution {
public:
    int longestConsecutive(vector<int> &num) {
       unordered_set<int> hashSet(num.begin(),num.end());
       int result=1;
       for(int current:num){
           if(hashSet.find(current)==hashSet.end()){
               continue;
           }
           hashSet.erase(current);
           int prev=current-1;
           int post=current+1;
           while(hashSet.find(prev)!=hashSet.end()){
               hashSet.erase(prev);
               prev--;
           }
           while(hashSet.find(post)!=hashSet.end()){
               hashSet.erase(post);
               post++;
           }
           result=max(result,post-prev-1);
       }
        return result;
    }
};

```

# analysis
>首先建立一个hash表，然后初始化存储所有的数据元素。遍历数组，然后去找相关的hash表的值，如果找到了，就删除，并且重复遍历其相邻的hash表的值。就行了
# reference
[[编程题]longest-consecutive-sequence][1]

[1]: https://www.nowcoder.com/questionTerminal/57d83a2501164168841c158a7535b458
