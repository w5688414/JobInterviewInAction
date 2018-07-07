# problem
>In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.
Example 1:
```
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```
Note:
1. The input will only have lower-case letters.
2. 1 <= dict words number <= 1000
3. 1 <= sentence words number <= 1000
4. 1 <= root length <= 100
5. 1 <= sentence words length <= 1000

# codes
```
class Solution {
public:
    string replaceWords(vector<string>& dict, string sentence) {
        istringstream is(sentence);
        vector<vector<string>> v(26);
        sort(dict.begin(),dict.end(),[](string a,string b){
           return a.size()<b.size(); 
        });
        for(string word:dict){
            v[word[0]-'a'].push_back(word);
        }
        string res;
        string t;
        while(is>>t){
            for(string word:v[t[0]-'a']){
                if(t.substr(0,word.size())==word){
                    t=word;
                    break;
                }
            }
            res+=t+' ';
        }
        res.pop_back();
        return res;
    }
};
```

# analysis
>我想了一个解法，没有通过，可能遇见了什么bug，找也找不出来，借鉴了别人的思路，还是挺清楚的，截取与dict中word相同长度的字符串进行比较，然后进行替换就行了。

# reference
[[LeetCode] Replace Words 替换单词][1]

[1]: http://www.cnblogs.com/grandyang/p/7423420.html