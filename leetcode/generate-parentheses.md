# problem
>Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"


# codes
```
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        DFS(n,n,"",result);
        return result;
    }
    void DFS(int left,int right,string temp,vector<string> &result){
        if(left>right){
            return ;
        }
        if(left==0&&right==0){
            result.push_back(temp);
        }else{
            if(left>0){
                DFS(left-1,right,temp+"(",result);
            }
            if(right>0){
                DFS(left,right-1,temp+")",result);
            }
        }
        
    }
};

```

# analysis
>这是一个深度优先搜索的题目，注意left代表剩余的左括号，right表示剩余的右括号；在任意时刻，左括号数目要大于右括号数目。
1）left大于right（left和right分别表示剩余左右括号的个数），即，临时变量中右括号的数大于左括号的数，则说明出现了“)(”，这是非法情况，返回即可；

2）left和right都等于0说明，临时变量中左右括号数相等，所以将临时变量中的值存入res中；

3）其余的情况是，先放左括号，然后放右括号，然后递归。注意参数的更新。

# reference
[[Leetcode] generate parentheses 生成括号][1]

[1]: https://www.cnblogs.com/love-yh/p/7159404.html