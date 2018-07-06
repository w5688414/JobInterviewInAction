# problem
>TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


# codes

```
class Solution {
private:
    unordered_map<string,string> short2long,long2short;
    string dict;
public:
    Solution(){
        dict = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        short2long.clear();
        long2short.clear();
        srand(time(NULL));
    }

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        if(long2short.count(longUrl)){
            return "http://tinyurl.com/" + long2short[longUrl];
        }
        string randStr;
        for(int i=0;i<6;i++){
            randStr.push_back(dict[rand()%62]);
        }
        int idx=0;
        while(short2long.count(randStr)){
            randStr[idx]=dict[rand()%62];
            idx=(idx+1)%5;
        }
        short2long[randStr]=longUrl;
        long2short[longUrl]=randStr;
        return "http://tinyurl.com/" + long2short[longUrl];
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        string randStr=shortUrl.substr(shortUrl.find_last_of("/")+1);
        return short2long.count(randStr) ? short2long[randStr]:shortUrl;
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));
```

# analysis
>这道题我也不怎么会，后面发现别人做得也是很简单的，encode阶段，如果该url已经编码了，则直接返回已经编码的url，如果没有，则生成随机数，然后判断随机数是否已经生成，如果生成了，则重新生成，然后存入url 的short long和long short的键值对。

# reference

[[LeetCode] Encode and Decode TinyURL 编码和解码精简URL地址][1]

[1]: http://www.cnblogs.com/grandyang/p/6562209.html