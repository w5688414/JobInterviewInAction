# problem
>输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同

# codes
```
class Solution {
public:
    vector<vector<int> > FindContinuousSequence(int sum) {
        vector<vector<int> > result;
        if(sum<3)
            return result;
        int cur_sum=1;
        int begin=1;
        int end=2;
        int mid=sum/2;
        cur_sum=begin+end;
        while(begin<=mid&&end<sum){
            while(cur_sum>sum){
                cur_sum-=begin;
                begin++;
            }
            if(cur_sum==sum){
                InsertResult(begin,end,result);
            }
            end++;
            cur_sum+=end;
            
        }
        return result;
    }
    void InsertResult(int begin,int end,vector<vector<int> > &result){
        vector<int> cur_result;
        for(int i=begin;i<=end;i++){
            cur_result.push_back(i);
        }
        result.push_back(cur_result);
    }
};
```
# analysis
>可能是最近变傻了，这道题居然都不会，本质上就是一个从头到尾遍历的过程，用cur_sum表示连续序列的和，begin表示开始的数，end表示结束的数，每遍历一步，如果cur_sum大于sum，begin++，相应的减去begin.如果等于,则符合条件，把序列存起来，继续搜索。其他cur_sum小于sum的情况，则end++，cur_sum加上相应的值。这样循环下去。

# reference
[[编程题]和为S的连续正数序列][1]

[1]: https://www.nowcoder.com/questionTerminal/c451a3fd84b64cb19485dad758a55ebe