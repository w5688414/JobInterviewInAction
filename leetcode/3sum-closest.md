# problem
> Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

```
    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

```
# codes
```
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        sort(num.begin(),num.end());
        int closet=num[0]+num[1]+num[2];
        int diff = abs(closet - target);
        for(int i=0;i<num.size()-2;i++){
            int left=i+1;
            int right=num.size()-1;
            while(left<right){
                int sum=num[i]+num[left]+num[right];
                int newDif=abs(sum-target);
                if(diff>newDif){
                    diff=newDif;
                    closet=sum;
                }
                if(sum<target){
                    left++;
                }else{
                    right--;
                }
            }
        }
        return closet;
    }
};
```

# analysis
>这道题目我开始想复杂了，结果都动不了笔，看完别人的解析后，发现还是遍历，然后不断更新现有的diff和closet.

# reference
[[LeetCode] 3Sum Closest 最近三数之和][1]

[1]:http://www.cnblogs.com/grandyang/p/4510984.html