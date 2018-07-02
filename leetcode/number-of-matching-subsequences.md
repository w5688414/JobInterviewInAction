# problem
>Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
```
Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
```
Note:

- All words in words and S will only consists of lowercase letters.
- The length of S will be in the range of [1, 50000].
- The length of words will be in the range of [1, 5000].
- The length of words[i] will be in the range of [1, 50].

# codes
```
class Solution {
public:
    int numMatchingSubseq(string S, vector<string>& words) {
        vector<vector<int>> alpha(26);
        for(int i=0;i<S.size();i++){
            alpha[S[i]-'a'].push_back(i);
        }
        int res=0;
        for(auto word:words){
            int x=-1;
            bool found=true;
            for(char c:word){
                auto it=upper_bound(alpha[c-'a'].begin(),alpha[c-'a'].end(),x);
                if(it==alpha[c-'a'].end()){
                    found=false;
                    break;
                }else{
                    x=*it;
                }
            }
            if(found){
                res++;
            }
        }
        return res;
    }
};
```

# analysis
>上面的思路是，用一个26位的数组alpha存储S种每个字符的索引。然后对于words，用二分法查找每个word中每个字符c的索引是否存在，如果二分查找找到了尾部，说明索引不存在，则这个单词就不是S的substring。对于这个怎么查找了我不怎么理解，这道题我也没有做出来，看来还需要锻炼一下。

upper_bound(a.begin(),a.end(),x)返回的是迭代器

# reference
[792. Number of Matching Subsequences][1]
[C++STL中的upper_bound()函数的使用][2]

[1]: https://leetcode.com/problems/number-of-matching-subsequences/discuss/117575/C++-12-Line-Solution-with-Explanation
[2]: https://blog.csdn.net/qq_30339595/article/details/79160715

