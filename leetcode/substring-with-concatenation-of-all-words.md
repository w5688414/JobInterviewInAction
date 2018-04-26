# problem
>You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S:"barfoothefoobarman"
L:["foo", "bar"]

You should return the indices:[0,9].
(order does not matter).

# codes
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

# analysis
>这道题目说实话，我做不出来。敲完别人的代码，发现只需要两个map就行了，其中一个map1记录每个单词的频率，然后遍历原字符串，由于单词是固定长度的，所以我们每次截取固定长度的单词，判断其是否在map1中，如果在，判断其是否有重复，所有第二个map2的作用就来了，我们用map2来记录其统计我们匹配的每个单词的频率，这样我们可以判断是否有重复，map2上的每个单词都在map1中，且不重复，这样就可以得到我们符合要求的子字符串的其实位置。

# reference
[[编程题]substring-with-concatenation-of-all-words][1]

[1]: https://www.nowcoder.com/questionTerminal/69ad067708c14c248f9cb9b7b6553e8f
