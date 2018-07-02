# problem
> Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
- You may assume that both strings contain only lowercase letters.
```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

# codes
```
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> m;
        for(auto c:magazine){
            m[c]++;
        }
        for(auto c:ransomNote){
            if(--m[c]<0) return false;
        }
        return true;
    }
};
```

# analysis
>开始我还以为要考虑顺序，推了dp，后面发现是我错了。好吧，再一次被打倒了，用一个map就搞定了。

# reference
[[LeetCode] Ransom Note 赎金条][1]


[1]: http://www.cnblogs.com/grandyang/p/5764314.html