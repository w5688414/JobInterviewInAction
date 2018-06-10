# problem
> 现在有 a 到 z 26 个元素， 编写程序打印 a 到 z 中任取 3 个元素的组合（比如 打印 a b c ，d y z等）

# codes
```
#include <iostream>
using namespace std;

int bit(int x){
    int c=0;
    while(x){
        int a=x%2;
        if(a==1){
            c++;
        }
        x=x/2;
    }
    return c;
}

void print(int n,int count){
    if(bit(n)==count){
        for(int i=0;i<26;i++){
            if(n&1){
                cout<<char('a'+i);
            }
            n=(n>>1);
        }
        cout<<endl;
    }
    
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int N=26;
    int C=3;
    int X=(1<<N)-1;
    for(int i=0;i<X;i++){
        print(i,C);
    }
    return 0;
}

```

# analysis
>这道题我第一印象就是三重循环解决，后面发现居然1<<26的数遍历一遍就行了，真是不可思议，解法挺新颖的。

# reference
[一道百度机器学习工程师职位的面试题][1]

[1]:https://blog.csdn.net/lvonve/article/details/53320680