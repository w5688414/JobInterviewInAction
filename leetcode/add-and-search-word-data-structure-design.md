# problem
> Design a data structure that supports the following two operations:
```
void addWord(word)
bool search(word)
```
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
Example:
```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```
Note:
You may assume that all words are consist of lowercase letters a-z.

# codes
```
class WordDictionary {

public:
    struct TrieNode{
        TrieNode* child[26];
        bool isWord;
        TrieNode():isWord(false){
            for(auto& a:child){
                a=NULL;
            }
        }
    };
    /** Initialize your data structure here. */
    WordDictionary() {
        root=new TrieNode();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        TrieNode *p=root;
        for(auto& a:word){
            int i=a-'a';
            if(!p->child[i]) p->child[i]=new TrieNode();
            p=p->child[i];
        }
        p->isWord=true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return search(word,root,0);
    }
    
    bool search(string word,TrieNode* p,int i){
        if(i==word.size()) return p->isWord;
        if(word[i]=='.'){
            for(auto& a:p->child){
                if(a&&search(word,a,i+1)) return true;
            }
            return false;
        }else{
            return p->child[word[i]-'a']&&search(word,p->child[word[i]-'a'],i+1);
        }
    }
private:
    TrieNode *root;
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * bool param_2 = obj.search(word);
 */
```

# analysis
>这道题用了wordtree的结构，如果不是刷leetcode，我可能就不了解这个东西了，希望以后我能独立的写出来。

# reference
[[LeetCode] Add and Search Word - Data structure design 添加和查找单词-数据结构设计][1]

[1]: http://www.cnblogs.com/grandyang/p/4507286.html