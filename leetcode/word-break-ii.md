# problem
>Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s ="catsanddog", 
dict =["cat", "cats", "and", "sand", "dog"].

A solution is["cats and dog", "cat sand dog"].
# codes
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

# analysis
>首先采用动态规划算出句子所有子串是否是字典中的内容，保存在二维数组中。dp行代表子串起始的下标，列表示字串长度-1.

#reference 
[[编程题]word-break-ii][1]
[1]: https://www.nowcoder.com/questionTerminal/bd73f6b52fdc421d91b14f9c909f9104