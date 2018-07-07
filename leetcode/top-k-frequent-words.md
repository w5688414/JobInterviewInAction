# problem
>Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
Example 1:
```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```
Example 2:
```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```
Note:
1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
2. Input words contain only lowercase letters.
Follow up:
1. Try to solve it in O(n log k) time and O(n) extra space.

# codes
```
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        vector<string> res;
        unordered_map<string,int> fre;
        map<int,set<string>> m;
        for(string word:words){
            fre[word]++;
        }
        for(auto f:fre){
            m[f.second].insert(f.first);
        }
        for(auto it=m.rbegin();it!=m.rend();it++){
            if(k<=0){
                break;
            }
            auto t=it->second;
            vector<string> v(t.begin(),t.end());
            if(k>=t.size()){
                res.insert(res.end(),v.begin(),v.end());
            }else{
                res.insert(res.end(),v.begin(),v.begin()+k);
            }
            k-=t.size();
        }
        return res;
    }
};
```

# analysis
>先计算词频，然后词频当作建，单词当作值。然后从词频最高的词倒序加入结果集合。

# reference
[[LeetCode] Top K Frequent Words 前K个高频词][1]

[1]: http://www.cnblogs.com/grandyang/p/7689927.html