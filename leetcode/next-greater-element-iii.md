# problem
>Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
```
Input: 12
Output: 21
```
Example 2:
```
Input: 21
Output: -1
```
# codes

## s1
```
class Solution {
public:
    int nextGreaterElement(int n) {
        string s=to_string(n);
        int m=s.length();
        int left=0;
        for(int i=m-1;i>0;i--){
            if(s[i]>s[i-1]){
                left=i-1;
                break;
            }
        }
        for(int i=m-1;i>0;i--){
            if(s[i]>s[left]){
                swap(s[i],s[left]);
                sort(s.begin()+left+1,s.end());
                break;
            }
        }
        long long res=stoll(s);
        if(res==n){
            return -1;
        }
        return res> INT_MAX ? -1:res;
    }
};
```

# analysis
>这个跟下一个排列那一题很像，要不是我做过那一题，这道题我应该没办法。

比如12443322，这个数字的重排序结果应该为13222344，如果我们仔细观察的话会发现数字变大的原因是左数第二位的2变成了3，细心的童鞋会更进一步的发现后面的数字由降序变为了升序，这也不难理解，因为我们要求刚好比给定数字大的排序方式。那么我们再观察下原数字，看看2是怎么确定的，我们发现，如果从后往前看的话，2是第一个小于其右边位数的数字，因为如果是个纯降序排列的数字，做任何改变都不会使数字变大，直接返回-1。知道了找出转折点的方法，再来看如何确定2和谁交换，这里2并没有跟4换位，而是跟3换了，那么如何确定的3？其实也是从后往前遍历，找到第一个大于2的数字交换，然后把转折点之后的数字按升序排列就是最终的结果了。最后记得为防止越界要转为长整数型，然后根据结果判断是否要返回-1即可

stoll: Convert string to long long

# reference
[[LeetCode] Next Greater Element III 下一个较大的元素之三][1]

[1]: http://www.cnblogs.com/grandyang/p/6716130.html
