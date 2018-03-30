# problem
> 堆排序的实现
# codes
```
#include<iostream>
using namespace std;

void adjust(int arr[],int len,int index){
    int left=2*index+1;
    int right=2*index+2;
    int maxIdx=index;    // maxIdx是3个数中最大数的下标
    if(left<len&&arr[left]>arr[maxIdx]) maxIdx=left;
    if(right<len&&arr[right]>arr[maxIdx]) maxIdx=right;
    if(maxIdx!=index){  // 如果maxIdx的值有更新
        swap(arr[maxIdx],arr[index]);
        adjust(arr,len,maxIdx); // 递归调整其他不满足堆性质的部分
    }
}

void heapSort(int arr[],int size){
    for(int i=size/2-1;i>=0;i--){
        adjust(arr,size,i);
    }
    for(int i=size-1;i>=1;i--){
        swap(arr[0],arr[i]);
        adjust(arr,i,0);
    }
}

int main(){
    int array[8]={8, 1, 14, 3, 21, 5, 7, 10};
    heapSort(array,8);
    for(auto it: array)
    {
        cout<<it<<endl;
    }

    return 0;
}

```

# analysis
>建堆(初始化+调整堆, 时间复杂度为O(n));
拿堆的根节点和最后一个节点交换(siftdown, 时间复杂度为O(n*log n) ).
建堆复杂度
证明方法如下： 
1. 假设根节点的高度为0，叶子节点高度为h，那么每层包含的元素个数为2^x，x从0到h。 
2. 构建堆的过程是自下而上，对于每层非叶子节点需要调整的次数为h-x，因此很明显根节点需要调整(h-0)次，第一层节点需要调整(h-1)次，最下层非叶子节点需要调整1次。 
3. 因此可知，构造树高为h的二叉堆精确时间复杂度为： 
s = 1*2^(h-1) + 2*2^(h-2)+……+h*2^0

可以看出以上公式是等差数列和等比数列乘积之和，可以通过错位相减求： 
2s = 2^h + 2*2^(h-1)+3*2^(h-2)+……+h*2^1
因此可得: 
s = 2s -s = 2^h + 2^(h-1) + 2^(h-2) +…… + 2^1 - h

最终可以通过等比数列公式进行计算得到s = 2*2^h - 2 -h 
h=log2(n)
代入的s = 2n - 2 - log2(n)，近似的时间复杂度就是O(n)。

# reference
[堆排序原理及其实现(C++)][1]
[构建堆的时间复杂度][2]

[1]: https://blog.csdn.net/lzuacm/article/details/52853194
[1]: https://blog.csdn.net/hupenghui1224/article/details/57427045