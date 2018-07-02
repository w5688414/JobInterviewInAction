# problem
>You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example 1:
```
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
```
Example 2:
```
Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
```

# codes

## s1
```
class Solution {
public:
    vector<int> findSubstring(string S, vector<string> &L) {
        unordered_map<string, int> counts;//存储每个单词的次数
        for(string words:L){
            counts[words]++;
        }
        int n=S.length();
        int num=L.size();
        int len=L[0].size();
        vector<int> indexes;
        //i代表起点
        for(int i=0;i<n-num*len+1;i++){
            unordered_map<string, int> seen; //存储i为起点的字符串里指定单词的次数
            int j=0; //表示单词数目，只有当j==num时，才找到了所有单词
            for(;j<num;j++){
                string word=S.substr(i+j*len,len);  //以i为起点，长度为len的第j个单词
                if(counts.find(word)!=counts.end()){
                    seen[word]++;
                    if(seen[word]>counts[word]){ //如果此单词出现次数超出，则i位置不合法
                        break;
                    }
                }else{
                    break;
                }
            }
            if(j==num){
                indexes.push_back(i);
            }
        }
        return indexes;
    }
};

```
## s2
```
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        if(s.empty()||words.empty()){
            return res;
        }
        int m=words.size();
        int n=words[0].size();
        unordered_map<string,int> m1;
        for(auto word:words){
            m1[word]++;
        }
        int len=s.length();
        for(int i=0;i<=len-m*n;i++){
            unordered_map<string,int> m2;
            int j=0;
            for(;j<m;j++){
                string t=s.substr(i+j*n,n);
                if(m1.find(t)==m1.end()){
                    break;
                }
                m2[t]++;
                if(m2[t]>m1[t]){
                    break;
                }
            }
            if(j==m){
                res.push_back(i);
            }
        }
        return res;
    }
};
```

# analysis

## s1
>这道题目说实话，我做不出来。敲完别人的代码，发现只需要两个map就行了，其中一个map1记录每个单词的频率，然后遍历原字符串，由于单词是固定长度的，所以我们每次截取固定长度的单词，判断其是否在map1中，如果在，判断其是否有重复，所有第二个map2的作用就来了，我们用map2来记录其统计我们匹配的每个单词的频率，这样我们可以判断是否有重复，map2上的每个单词都在map1中，且不重复，这样就可以得到我们符合要求的子字符串的起始位置。

## s2
第二遍感觉跟第一遍差不多，还是没想出来，算是又预习了一遍吧。依旧是两个map，第一个map统计词频
，第二个map统计截取的字符串的词频，然后做比较。

# reference
[[编程题]substring-with-concatenation-of-all-words][1]
[[LeetCode] Substring with Concatenation of All Words 串联所有单词的子串][2]

[1]: https://www.nowcoder.com/questionTerminal/69ad067708c14c248f9cb9b7b6553e8f
[2]: http://www.cnblogs.com/grandyang/p/4521224.html