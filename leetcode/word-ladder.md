# problem
>Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start ="hit"
end ="cog"
dict =["hot","dot","dog","lot","log"]

As one shortest transformation is"hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length5.

Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

# codes
```
class Solution {
public:
    int ladderLength(string start, string end, unordered_set<string> &dict) {
        dict.insert(end);
        dict.erase(start);
        queue<string> q;
        q.push(start);
        vector<string> deleteList;
        int length=0;
        while(!q.empty()){
            length++;
            int queuelength=q.size();
            for(int j=0;j<queuelength;j++){
                start=q.front();
                q.pop();
                if(start==end){
                    return length;
                }
                for(unordered_set<string>:: iterator iter=dict.begin();iter!=dict.end();iter++){
                    int dis=distance(start,*iter);
                    if(dis==1){
                        q.push(*iter);
                        deleteList.push_back(*iter);
                    }
                }
                for(int i=0;i<deleteList.size();i++){
                    dict.erase(deleteList[i]);
                }
                deleteList.clear();
            }
        }
        return 0;
    }
    int distance(string s1,string s2){
        int count=0;
        for(int i=0;i<s1.size();i++){
            if(s1[i]!=s2[i]){
                count++;
            }
        }
        return count;
    }
};

```

# analysis
>本题用了一个队列，先把start放进去，然后每次从队列里面取字符串，计算字符串与词典之间的距离，如果距离为1，我们就把字符串加入队列，然后长度+1，这样一直遍历到队列为空为止。

# reference
[[编程题]word-ladder][1]

[1]: https://www.nowcoder.com/questionTerminal/bd75ae43ff7148548eb4701550df2714