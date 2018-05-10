# problem
> Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
```
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
```
# codes
```
class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
        vector<vector<int>> result;
        if(nums.size()<3){
            return result;
        }
        set<vector<int> > res;
        sort(num.begin(),num.end());
        for(int i=0;i+2<num.size();i++){
           if(i>0&&num[i]==num[i-1])
                continue;
            int left=i+1;
            int right=num.size()-1;
            while(left<right){
                int sum=num[i]+num[left]+num[right];
                if(sum==0){
                    vector<int> temp{num[i],num[left],num[right]};
                    res.insert(temp);
                    left++;
                    right--;
                }else if(sum<0){
                    left++;
                }else{
                    right--;
                }
            }
        }
        return vector<vector<int> > (res.begin(),res.end());
    }
};
```

# analysis
>我发现循环的时候只要num.size()-2，就会报错，不清楚这是啥情况，很常规的做法，弄懂了4sum，3sum就会了。

# reference
[[编程题]3sum][1]

[1]:https://www.nowcoder.com/questionTerminal/345e2ed5f81d4017bbb8cc6055b0b711