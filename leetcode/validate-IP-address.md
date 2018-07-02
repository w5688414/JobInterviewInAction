# problem
>Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
```
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
```
Example 2:
```
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
```
Example 3:
```
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
```
# codes
```
class Solution {
public:
    string validIPAddress(string IP) {
        istringstream is(IP);
        string  t="";
        int cnt=0;
        if(IP.find(":")==string::npos){
            while(getline(is, t, '.')){ // Check IPv4
                ++cnt;
                if(cnt>4||t.empty()||(t.size()>1&&t[0]=='0')||t.size()>3){
                    return "Neither";
                }
                for(char c:t){
                    if(c<'0'||c>'9'){
                        return "Neither";
                    }
                }
                int val=stoi(t);
                if(val<0||val>255){
                    return "Neither";
                }
            }
            return cnt==4&&IP.back()!='.' ? "IPv4":"Neither";
        }else{  // Check IPv4
            while(getline(is,t,':')){
                ++cnt;
                if(cnt>8||t.empty()||t.size()>4){
                    return "Neither";
                }
                for(char c:t){
                    if(!(c>='0'&&c<='9')&&!(c>='a'&&c<='f')&&!(c>='A'&&c<='F')){
                        return "Neither";
                    }
                }
            }
            return cnt==8&&IP.back()!=':' ? "IPv6":"Neither";
        }
    }
};
```

# analysis
>说实话，我觉得C++判断字符串是否合法，有点麻烦，今天就学习了我比较陌生的函数，好吧，我又孤陋寡闻了。
判断是否是IPv4和IPv6，感觉还是比较麻烦的事情。

C标准函数库中的头文件 ctype.h中

注意：

查找字符串a是否包含子串b,不是用strA.find(strB) > 0 而是 strA.find(strB) != string:npos

其中string:npos是个特殊值，说明查找没有匹配

# reference
[[LeetCode] Validate IP Address 验证IP地址][1]
[字符串的查找删除---C++中string.find()函数与string::npos][2]


[1]: http://www.cnblogs.com/grandyang/p/6185339.html
[2]: https://www.cnblogs.com/Miranda-lym/p/6357395.html