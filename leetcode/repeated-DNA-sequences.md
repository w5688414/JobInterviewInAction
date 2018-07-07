# problem
>All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

# codes
```
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_set<string> res,st;
        for(int i=0;i+9<s.length();i++){
            string t=s.substr(i,10);
            if(st.count(t)){
                res.insert(t);
            }else{
                st.insert(t);
            }
        }
        return vector<string>(res.begin(),res.end());
    }
};
```

# analysis
>看懂题目后，用两个set集合就行了，好吧，我没看懂题目，还是太嫩了。

# reference
[[LeetCode] Repeated DNA Sequences 求重复的DNA序列][1]

[1]: http://www.cnblogs.com/grandyang/p/4284205.html