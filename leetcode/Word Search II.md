# problem
>Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
Example:
```
Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
```
Note:
You may assume that all inputs are consist of lowercase letters a-z.

Hint:

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.


# codes
```
class TrieNode{
public:
    int isWord;
    vector<TrieNode*> next;
    TrieNode(){
        isWord=-1;
        next=vector<TrieNode*>(26,NULL);
    }
};

class Solution {
private:
    TrieNode* root;
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        root=new TrieNode();
        buildTree(words,root);
        set<string> res;
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[i].size();j++){
                findWords(res,board,words,root,i,j);
            }
        }
        return vector<string>(res.begin(),res.end());
        
    }
    
    void findWords(set<string>& res, vector<vector<char>>& board, vector<string>& words, TrieNode* node, int r, int c){
        if(board[r][c] == '.' || !node->next[board[r][c]-'a']) return;
        TrieNode* after=node->next[board[r][c]-'a'];
        if(after->isWord>-1){
            res.insert(words[after->isWord]);
        }
        char letter=board[r][c];
        board[r][c]='.';
        if(r-1>=0){
            findWords(res,board,words,after,r-1,c);
        }
        if(r+1<board.size()){
            findWords(res,board,words,after,r+1,c);
        }
        if(c-1>=0){
            findWords(res,board,words,after,r,c-1);
        }
        if(c+1<board[0].size()){
            findWords(res,board,words,after,r,c+1);
        }
        board[r][c]=letter;
        
    }
    
    void buildTree(vector<string>& words,TrieNode* root){
        TrieNode* cur;
        for(int i=0;i<words.size();i++){
            cur=root;
            for(char c:words[i]){
                if(!cur->next[c-'a']){
                    cur->next[c-'a']=new TrieNode();
                }
                cur=cur->next[c-'a'];
            }
            cur->isWord=i;
        }
    }
};
```

# analysis
>首先建立了一个trie的树，然后在这个字典树里面查找。

# reference
[212. Word Search II][1]

[1]: https://leetcode.com/problems/word-search-ii/description/