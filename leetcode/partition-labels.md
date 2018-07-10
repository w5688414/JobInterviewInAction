# problem
>
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```
Note:

1. S will have length in range [1, 500].
2. S will consist of lowercase letters ('a' to 'z') only.

# codes
```
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> res;
        int n=S.size();
        int start=0;
        int last=0;
        unordered_map<char,int> m;
        for(int i=0;i<n;i++){
            m[S[i]]=i;
        }
        for(int i=0;i<n;i++){
            last=max(last,m[S[i]]);
            if(i==last){
                res.push_back(i-start+1);
                start=i+1;
            }
        }
        return res;
    }
};
```

# analysis

用hash表建立字母和其最后出现位置之间的映射，那么对于题目中的例子来说，我们可以得到如下映射：

a -> 8
b -> 5
c -> 7
d -> 14
e -> 15
f -> 11
g -> 13
h -> 19
i -> 22
j -> 23
k -> 20
l -> 21

建立好映射之后，就需要开始遍历字符串S了，我们维护一个start变量，是当前子串的起始位置，还有一个last变量，是当前子串的结束位置，每当我们遍历到一个字母，我们需要在HashMap中提取出其最后一个位置，因为一旦当前子串包含了一个字母，其必须包含所有的相同字母，所以我们要不停的用当前字母的最后一个位置来更新last变量，只有当i和last相同了，即当i = 8时，当前子串包含了所有已出现过的字母的最后一个位置，即之后的字符串里不会有之前出现过的字母了，此时就应该是断开的位置，我们将长度9加入结果res中，同理类推，我们可以找出之后的断开的位置，

# reference
[[LeetCode] Partition Labels 分割标签][1]

[1]: https://www.cnblogs.com/grandyang/p/8654822.html