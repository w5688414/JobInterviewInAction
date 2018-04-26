# problem
>Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# codes
```
class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        for(int i = 0; i < n; i++){
             if(A[i] == elem){
                 swap(A[i--], A[--n]);
             }
         }
        return n;
    }
};
```

# analysis
- 我写的就有问题，别人写的都对，不明白啥情况。


# reference
[[编程题]remove-element][1]

[1]: https://www.nowcoder.com/questionTerminal/1e1b7d86039e4427b4b6f7cbb856c301