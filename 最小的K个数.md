# problem
>输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,
# codes
```
class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
         vector<int> result;
         if(input.size()<k)
             return result;
         for(int i=0;i<k;i++){
             heapSort(input,i, input.size()-1);
             result.push_back(input[i]);
         }
        return result;
        
    }
    void heapSort(vector<int> &input,int root, int end){
        for(int j=end;j>=root;j--){
            int parent=(j+root-1)/2;
            if(input[parent]>input[j]){
                swap(input[parent],input[j]);
            }
        }
    }
   
};

```

# analysis
>这一题是关于堆排序的一个题目，用最大堆。从最后一个元素开始，依次和堆的parent比较，遍历完后就得到第一个最小值；第二次遍历会得到第二个最小值，依次类推。
# reference
[[编程题]最小的K个数][1]

[1]: https://www.nowcoder.com/questionTerminal/6a296eb82cf844ca8539b57c23e6e9bf