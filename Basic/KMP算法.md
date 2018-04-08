# problem
>一、问题描述：

对于两个字符串S、T，找到T在S中第一次出现的起始位置，若T未在S中出现，则返回-1。

二、输入描述：

两个字符串S、T。

三、输出描述：

字符串T在S中第一次出现的起始位置，若未出现，则返回-1。

四、输入例子：

ababaababcb
ababc

五、输出例子：

5

# codes
```
#include<iostream>
#include<vector>
#include<string.h>

using namespace std;

vector<int> getNext(string T){
    vector<int> next(T.size(),0);  // next矩阵，含义参考王红梅版《数据结构》p84
    next[0]=-1;   // next矩阵的第0位为-1
    int k=0; // k值
    for(int j=2;j<T.size();j++){ // 从字符串T的第2个字符开始，计算每个字符的next值
        while(k>0&&T[j-1]!=T[k]){
            k=next[k];
        }
        if(T[j-1]==T[k])
            k++;
        next[j]=k;
    }
    return next;  // 返回next矩阵
}
int KMP(string S, string T){
    vector<int> next=getNext(T);
    int i=0,j=0;
    while(S[i]!='\0'&&T[j]!='\0'){
        if(S[i]==T[j]){
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
    if(T[j]=='\0')
        return i-j;
    else
        return -1;
}

int main(){
    string S="ababaababcb";
    string T="ababc";
    int num=KMP(S,T);
    cout<<num<<endl;
    return 0;
}

```

# analysis
>1. 在串S和串T中分别设置比较的起始下标i和j;
2. 重复下述操作，直到S或T的所有字符均比较完毕;
    2.1 如果S[i]等于T[j]，继续比较S和T的下一对字符;
    2.2 否则将下标j回溯到next[j]的位置，即j = next[j];
    2.3 如果j等于-1，则将下标i和j分别加1，准备下一趟比较;
3. 如果T中所有字符均比较完毕，则返回匹配的i-j;
    否则返回-1;
# reference
[字符串模式匹配KMP算法中的next数组算法及C++实现][1]

[1]: https://www.cnblogs.com/renjiashuo/p/6896062.html
