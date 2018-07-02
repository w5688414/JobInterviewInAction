# problem
>Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
```
Input: "Hello, my name is John"
Output: 5
```

# codes
```
class Solution {
public:
    int countSegments(string s) {
        int cnt=0;
        int n=s.length();
        for(int i=0;i<s.length();i++){
            if(s[i]==' ') continue;
            cnt++;
            while(i<n&&s[i]!=' ') i++;
        }
        return cnt;
    }
};
```

# analysis
>这道题我虽然能做，但是A不全，总是会出错。没想到反过来我们过滤掉空格字符和非空格字符，然后只计算迭代的次数就行了，很神奇。

# reference
[[LeetCode] Number of Segments in a String 字符串中的分段数量][1]


[1]: http://www.cnblogs.com/grandyang/p/6137386.html


