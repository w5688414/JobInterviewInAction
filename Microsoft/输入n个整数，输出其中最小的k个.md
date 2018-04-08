# problem
>

输入n个整数，输出其中最小的k个。

详细描述：

接口说明

原型：

bool GetMinK(unsignedint uiInputNum, int * pInputArray, unsignedint uiK, int * pOutputArray);

输入参数：

     unsignedint uiInputNum //输入整数个数

int * pInputArray  //输入整数数组

unsignedint uiK   //需输出uiK个整数

输出参数（指针指向的内存区域保证有效）：

    int * pOutputArray //最小的uiK个整数

返回值：

        false 异常失败

          true  输出成功

# codes
```
#include<iostream>
using namespace std;
 
int main()
{
    int n,m;
    while(cin>>n>>m)
    {
        int *p;
        p=new int[n];
        for(int i=0;i<n;i++)
        {
            cin>>p[i];
        }
 
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n-i-1;j++)
            {
                if(p[j]>p[j+1])
                {
                    int t=p[j];
                    p[j]=p[j+1];
                    p[j+1]=t;
                }
            }
        }
 
        for(int k=0;k<m-1;k++)
        {
            cout<<p[k]<<'\40';
        }
        cout<<p[m-1]<<endl;
    }
    return 0;
}



```

# analysis
>首先接受字符串数组输入，然后从第0个字符串开始判断，利用回溯法，来找第0个最后一个字符，跟后面字符串的第一个字符相等的串，如果没找到，就回溯，然后遍历第1个字符串，找出与第0个末尾跟第1个串的第一个字符相同的串。
# reference
[判断字符串数组能否首尾相连][1]
[HDOJ-1181 字符串首尾相连问题[DFS（）+字符串排序strcmp（）||▲矩阵标记]][2]

[1]: https://blog.csdn.net/lmq_begood/article/details/52275570
[2]: https://www.cnblogs.com/XBWer/archive/2012/06/20/2555719.html
