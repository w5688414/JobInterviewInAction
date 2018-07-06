# problem
> Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
1. Input contains only lowercase English letters.
2. Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
3. Input length is less than 50,000.

Example 1:
```
Input: "owoztneoer"

Output: "012"
```
Example 2:
```
Input: "fviefuro"

Output: "45"
```

# codes
```
class Solution {
public:
    string originalDigits(string s) {
        string res="";
        vector<string> words={"zero","two","four","six","eight","one","three","five","seven","nine"};
        vector<int> nums{0,2,4,6,8,1,3,5,7,9},counts(26,0);
        vector<char> chars{'z','w','u','x','g','o','h','f','s','i'};
        for(char c:s) ++counts[c-'a'];
        for(int i=0;i<words.size();i++){
            int cnt=counts[chars[i]-'a'];
            for(int j=0;j<words[i].size();j++){
                counts[words[i][j]-'a']-=cnt;
            }
            while(cnt--){
                res+=nums[i]+'0';
            }
        }
        sort(res.begin(),res.end());
        return res;
    }
};
```

# analysis
- 仔细观察这些表示数字的单词"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"，我们可以发现有些的单词的字符是独一无二的，比如z，只出现在zero中，还有w，u，x，g这四个单词，分别只出现在two，four，six，eight中，那么这五个数字的个数就可以被确定了
- 由于含有o的单词有zero，two，four，one，其中前三个都被确定了，那么one的个数也就知道了;
- 由于含有h的单词有eight，three，其中eight个数已知，那么three的个数就知道了;
- 由于含有f的单词有four，five，其中four个数已知，那么five的个数就知道了;
- 由于含有s的单词有six，seven，其中six个数已知，那么seven的个数就知道了;
- 由于含有i的单词有six，eight，five，nine，其中前三个都被确定了，那么nine的个数就知道了;
- 我们按这个顺序"zero", "two", "four", "six", "eight", "one", "three", "five", "seven", "nine"就能找出所有的个数了.

# reference
[[LeetCode] Reconstruct Original Digits from English 从英文中重建数字][1]


[1]: http://www.cnblogs.com/grandyang/p/5996239.html