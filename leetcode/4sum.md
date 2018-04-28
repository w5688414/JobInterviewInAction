# problem
> Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.

```
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
```
# codes
```
class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        set<vector<int>> result;
        sort(num.begin(),num.end());
        vector<int> ans;
        for(int i=0;i<int(num.size()-3);i++){
            for(int j=i+1;j<int(num.size()-2);j++){
                if(j>i+1&&num[j]==num[j-1]){
                    continue;
                }
                int left=j+1;
                int right=num.size()-1;
                while(left<right){
                    int sum=num[i]+num[j]+num[left]+num[right];
                    if(sum==target){
                        vector<int> out{num[i],num[j],num[left],num[right]};
                        result.insert(out);
                        ++left;
                        --right;
                    }else if(sum<target){
                        ++left;
                    }else{
                        --right;
                    }
                }
            }
        }
        return vector<vector<int>>(result.begin(), result.end());
    }
    
};
```

# analysis
>这里的思路也很简单，先对num排序，然后遍历num，找到符合条件的四个数，然后放在set集合里面，set有一个好处是，它可以去重，这样就得到了所有的答案。这里注意int(num.size()-3)需要加上int，不然会不通过，具体原因未知。

# reference
[[编程题]4sum][1]

[1]: https://www.nowcoder.com/questionTerminal/eb632e81417c4d5797cd712b82f7daa1