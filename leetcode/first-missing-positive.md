# problem
>Given an unsorted integer array, find the first missing positive integer.

For example,
Given[1,2,0]return3,
and[3,4,-1,1]return2.

Your algorithm should run in O(n) time and uses constant space.

# codes
```
class Solution {
public:
    int firstMissingPositive(int A[], int n) {
        int i=0;
        while(i<n){
            while(A[i]>0&&A[i]<=n&&A[A[i]-1]!=A[i]){
                swap(A[i],A[A[i]-1]);
            }
            i++;
        }
        for(int j=0;j<n;j++){
            if(A[j]!=j+1){
                return (j+1);
            }
        }
        return n+1;
    }
};
```

# analysis
>这道题目似曾相识，最后一刻我想出来了，但是做错了，没有考虑到A[i]>=n和{1,2,2,4}这种情况，看来以后要多加练习。

# reference
[[编程题]first-missing-positive][1]
[1]: https://www.nowcoder.com/questionTerminal/ea7ca311264d4c579a1ef6c1f7f69138