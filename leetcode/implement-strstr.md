# problem
>Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.


# codes

##  problem one ac不了
```
class Solution {
public:
    char *strStr(char *haystack, char *needle) {
        int m=strlen(haystack);
        int n=strlen(needle);
        if(m<n){
            return NULL;
        }
        if(m==0&&n==0){
            return "";
        }
        vector<int> next=getNext(needle);
        int i=0,j=0;
        while(haystack[i]!='\0'&&needle[j]!='\0'){
            if(haystack[i]==needle[j]){
                i++;
                j++;
            }else{
                j=next[j];
            }
            if(j==-1){
                ++i;
                ++j;
            }
        }
        
        if(needle[j]=='\0'){
            char *p=&haystack[i-j];
            return p;
        }
        else
            return NULL;
        
    }
    
    vector<int> getNext(char *needle){
        int len=strlen(needle);
        vector<int> next(len,0);
        next[0]=-1;
        int k=0;
        for(int j=2;j<len;j++){
            while(k>0&&needle[j-1]!=needle[k]){
                k=next[k];
            }
            if(needle[j-1]==needle[k]){
                k++;
            }
            next[j]=k;
        }
        return next;
    }
};
```

## solution 2
```
class Solution {
public:
    char *strStr(char *haystack, char *needle) {
        int m=strlen(haystack);
        int n=strlen(needle);
        if(m<n){
            return NULL;
        }
        if(m==0&&n==0){
            return "";
        }
        int j=0;
        for(int i=0;i<=m-n;i++){
            for(int k=i;k<i+n;k++){                
                if(haystack[k]!=needle[j]){
                    j=0;
                    break;
                }
                j++;
            }
            if(needle[j]=='\0'){
                return &haystack[i];
            }
        }
        return NULL;
    } 
};
```

## s3
```
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty()){
            return 0;
        }
        int m=haystack.length();
        int n=needle.length();
        for(int i=0;i<=m-n;i++){
            bool flag=true;
            for(int j=0;j<n;j++){
                if(haystack[i+j]!=needle[j]){
                    flag=false;
                    break;
                }
            }
            if(flag){
                return i;
            }
        }
        return -1;
    }
};
```
# analysis
> KMP算法目前还没有调通，暴力破解版本已经AC了。
## s3
 又做了一次暴力算法，KMP算法仍没有尝试。
 
# reference
[[编程题]implement-strstr][1]
[[LeetCode] Implement strStr() 实现strStr()函数][2]

[1]: https://www.nowcoder.com/questionTerminal/cc0c03ec17ad44c09d25870c301e0db7
[2]: http://www.cnblogs.com/grandyang/p/4606696.html