# problem
>Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
Examples:
```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

# codes
```
class Solution {
public:
    string decodeString(string s) {
        int i=0;
        return decode(s,i);
    }
    string decode(string s,int &i){
        int n=s.length();
        string res="";
        while(i<n&&s[i]!=']'){
            if(s[i]<'0'||s[i]>'9'){
                res+=s[i];
                i++;
            }else{
                int count=0;
                while(s[i]>='0'&&s[i]<='9'){
                    count=count*10+s[i]-'0';
                    i++;
                }
                i++;
                string t=decode(s,i);
                i++;
                while(count--){
                    res+=t;
                }
            }
        }
        return res;
    }
};
```

# analysis
>这是一个递归的解法，我也没有想出来。首先如果是字母的话，我们就直接加入res中，如果不是，那就可能是数字，左中括号。如果是数字，我们先计算出数字的值，数字之后必然是左中括号，然后我们跳过它，去递归解码左中括号里面的串，递归回来后，我们分析一下返回条件，要么是到了s的末尾，要么就是遇见右中括号了，于是我们i++，即要么跳过右中括号，要么就到末尾了，然后把t*count倍的字符串加入res中。

# reference
[[LeetCode] Decode String 解码字符串][1]

[1]: https://www.cnblogs.com/grandyang/p/5849037.html