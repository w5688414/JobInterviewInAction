# problem
>Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s ="catsanddog", 
dict =["cat", "cats", "and", "sand", "dog"].

A solution is["cats and dog", "cat sand dog"].
# codes
## solution 1
```
class Solution {
private:
    vector<string> result;
    vector<string> mystring;
    vector<bool> *dp;
public:
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        dp = new vector<bool>[s.size()];
        for(int i=0;i<s.size();i++){
            for(int j=i;j<s.size();j++){
                dp[i].push_back(match(s.substr(i, j - i + 1), dict));
            }
        }
        output(s.size() - 1, s);
        return result;
    }
    
    bool match(string s, unordered_set<string> &dict){
        if(dict.find(s)!=dict.end()){
            return true;
        }else{
            return false;
        }
    }
    
    void output(int i,string s){
        if(i==-1){
            string str;
            for(int j=mystring.size()-1;j>=0;j--){
                str+=mystring[j]; 
                if(j!=0){
                    str+=" ";
                }
            }
            result.push_back(str);
        }else{
            for(int k=i;k>=0;k--){
                if(dp[k][i-k]){
                    mystring.push_back(s.substr(k, i - k + 1)); //dp[k][i-k]:偏移为k，截断长度i-k+1
                    output(k - 1, s);   //递归:dp[0][i]:偏移为0，截断长度i+1      i=k-1,则截断长度为k,与递归前偏移k互补
                    mystring.pop_back();
                }
            }
        }
    }
};
```

## solution 2
```
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(),wordDict.end());
        vector<bool> possible(s.size()+1,true);
        vector<string> ans;
        string item;
        dfs(s,0,dict,possible,ans,item);
        return ans;
    }
    
    bool dfs(string s,int index,unordered_set<string> dict, vector<bool> &possible, vector<string> &ans, string item){
        bool res=false;
        if(index==s.size()){
            ans.push_back(item.substr(0,item.size()-1));  // remove space in the end
            return true;
        }
        
        for(int i=index;i<s.size();i++){
            string word=s.substr(index,i-index+1);
            if(dict.find(word)!=dict.end()&&possible[i+1]){
                item=item+word+" ";
                if(dfs(s,i+1,dict,possible,ans,item)){
                    res=true;
                }else{
                    possible[i+1]=false;
                }
                item.resize(item.size()-word.size()-1);
            }
        }
        return res;
    }
};
```

# analysis
>首先采用动态规划算出句子所有子串是否是字典中的内容，保存在二维数组中。dp行代表子串起始的下标，列表示字串长度-1.
方法二用了深度优先搜索，竟然也通过了，看来还是自己的功力不够，动态规划我确实没看懂。

#reference 
[[编程题]word-break-ii][1]
[140. Word Break II][2]
[1]: https://www.nowcoder.com/questionTerminal/bd73f6b52fdc421d91b14f9c909f9104
[2]: https://leetcode.com/problems/word-break-ii/discuss/122159/c++-dfs-solution
