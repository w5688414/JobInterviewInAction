# problem
>
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.
Example 1:
```
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
```
Note:

1. You may assume that all the inputs are consist of lowercase letters a-z.
2. For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
3. Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

# codes
```
class MagicDictionary {
private:
    unordered_map<int,vector<string>> m;
public:
    /** Initialize your data structure here. */
    MagicDictionary() {
        
    }
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        for(string word:dict){
            m[word.size()].push_back(word);
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        for(string str:m[word.size()]){
            int cnt=0,i=0;
            for(;i<word.size();i++){
                if(str[i]!=word[i]){
                    cnt++;
                    if(cnt>1){
                        break;
                    }
                }
            }
            if(i==word.size()&&cnt==1){
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * bool param_2 = obj.search(word);
 */
```

# analysis
> 用了一个hash表，用单词的size当作key，设计不错。我也做不出来，学习一下，努力加油。

# reference
[[LeetCode] Implement Magic Dictionary 实现神奇字典][1]

[1]: http://www.cnblogs.com/grandyang/p/7612918.html