# problem
>Given an absolute path for a file (Unix-style), simplify it.

For example,
path ="/home/", =>"/home"
path ="/a/./b/../../c/", =>"/c"

Corner Cases:
Did you consider the case where path ="/../"?
In this case, you should return"/".
Another corner case is the path might contain multiple slashes'/'together, such as"/home//foo/".
In this case, you should ignore redundant slashes and return"/home/foo".

# codes

## s1
```
class Solution {
public:
    string simplifyPath(string path) {
       vector<string> v1;      
        for(int j=0;j<path.size();j++){
            while(j<path.size()&&path[j]=='/'){ //去掉多余的/
                    j++;
            }
            if(j==path.size()){
                break;
            }
            string word;
            while(j<path.size()&&path[j]!='/'){
                word+=path[j];
                j++;
            }
            if(word=="."){
                continue;
            }else if(word==".."){
                if(v1.size()){
                    v1.pop_back();
                }
            }else{
                v1.push_back(word);
            }
        }
        string simple_path;
        if(v1.size()>0){
            for(int i=0;i<v1.size();i++){
                simple_path+="/"+v1[i];
            }
        }
        return v1.empty() ? "/": simple_path;
    }
};

```
## s2
```
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> v;
        int i=0;
        int n=path.length();
        while(i<n){
            while(i<n&&path[i]=='/'){
                i++;
            }
            if(i==n) break;
            int left=i;
            while(i<n&&path[i]!='/'){
                i++;
            }
            int right=i-1;
            string s=path.substr(left,right-left+1);
            if(s==".."){
                if(!v.empty()){
                    v.pop_back();
                }
            }else if(s!="."){
                v.push_back(s);
            }
        }
        string res="";
        for(auto s:v){
            res=res+"/"+s;
        }
        return v.empty() ? "/":res;
    }
};
```

# analysis
## s1
开始的时候用的while循环，可能有的情况没有考虑到，有些测试样例扔进去就变成了死循环，看来以后用for循环还靠谱一点。这是一个字符串的题目，就是根据斜线分离单词，用一个vector存起来，单后把路径拼接出来
## s2
另一个版本，换成了while

# reference
[[编程题]simplify-path][1]
[[LeetCode] Simplify Path 简化路径][2]

[1]: https://www.nowcoder.com/questionTerminal/393e5a246a7546d1b2e4d7719647b7d9
[2]: http://www.cnblogs.com/grandyang/p/4347125.html