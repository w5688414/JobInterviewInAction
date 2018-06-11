# problem
> Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example
```
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

```

# codes
```
class Solution {
public:
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        auto comp=[](const pair<int,int>&p1,const pair<int,int>& p2){
            return p1.first>p2.first||(p1.first==p2.first&&p1.second<p2.second);
        };
        sort(people.begin(),people.end(),comp);
        vector<pair<int,int>> result;
        for(auto &p:people){
            result.insert(result.begin()+p.second,p);
        }
        return result;
    }
};
```

# analysis
>解法如下例子：
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

排序后：

[[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]

交换顺序：

[[7,0], [6,1], [7,1], [5,0], [5,2], [4,4]]

[[5,0], [7,0], [6,1], [7,1], [5,2], [4,4]]

[[5,0], [7,0], [5,2], [6,1], [7,1], [4,4]]

[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
先根据first降序排序，然后再根据second升序排列；然后把每个元素插入到resultvector操作，注意插入的操作。
# reference
[406. Queue Reconstruction by Height][1]
[[LeetCode] Queue Reconstruction by Height 根据高度重建队列][2]

[1]: https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89348/6-lines-Concise-C++?page=1
[2]: https://www.cnblogs.com/grandyang/p/5928417.html
