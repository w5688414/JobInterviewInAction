# problem
>Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S ="ADOBECODEBANC"
T ="ABC"

Minimum window is"BANC".

Note: 
If there is no such window in S that covers all characters in T, return the emtpy string"".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

# codes
```
class Solution {
public:
    string minWindow(string S, string T) {
        string result;
        if(!S.size()||!T.size()){
            return result;
        }
        int left=0;
        int count=0;
        int min_len=S.size()+1;  //最小窗口，便于比较最后取最小的,初始化取最大
        map<char,int> Tmap;
        for(int i=0;i<T.size();i++){
            Tmap[T[i]]++;
        }
        //移动右边窗口
        for(int right=0;right<S.size();right++){
            if(Tmap.find(S[right])!=Tmap.end()){ //当窗口内部有T中的字符
                if(Tmap[S[right]]>0){
                    count++;
                }
                Tmap[S[right]]--;
                while(count==T.size()){
                    if(Tmap.find(S[left])!=Tmap.end()){
                        if(min_len>right-left+1){
                            min_len=right-left+1;
                            result=S.substr(left,right-left+1);
                        }
                        //舍弃窗口左边字符串，继续移动窗口
                        Tmap[S[left]]++;
                        if(Tmap[S[left]]>0){  //如果左边连续相同，则count不递减，窗口需要继续向右移动
                        {
                            count--;
                        }
                    }
                    left++; 
                }
            }
        }
        return result;
    }
};

```

# analysis
>这道题目我也做不出来，大概是人老了吧，开始left=0，right向后移动，Tmap是T的字符计数键值对，
>我们用一个count来计算截取的子串是否合法，当count==T.size，说明截取的子串已经包含所给定的子串，然后我们移动left找最小的子串

# reference
[[编程题]minimum-window-substring][1]

[1]: https://www.nowcoder.com/questionTerminal/c466d480d20c4c7c9d322d12ca7955ac