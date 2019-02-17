# problem
>Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
Example 1:
```
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
```
Example 2:
```
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

```

# codes

```
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> result;
        if(input.length()==0){
            return result;
        }
        
        for(int i=0;i<input.size();i++){
            if(input[i]<'0'){
                vector<int> left=diffWaysToCompute(input.substr(0,i));
                vector<int> right=diffWaysToCompute(input.substr(i+1));
                for(auto i1:left){
                    for(auto i2:right){
                        switch(input[i]){
                            case '+':
                                result.push_back(i1+i2);
                                break;
                            case '-':
                                result.push_back(i1-i2);
                                break;
                            case '*':
                                result.push_back(i1*i2);
                                break;
                        }
                    }
                }
            }
        }
        if(result.empty()){
            result.push_back(stoi(input));
        }
        return result;
    }
};
```

# analysis
题目的意思是：给你一个表达式，你可以任意加括号，要求返回所有可能计算的结果。
- 这道题首先会想到递归，把所有的情况都列举出来，我们从运算符分开，分为left，right两个分支，把两个分支的所有的计算结果合并，组合然后就可以满足题目的要求了。

# reference

[241. Different Ways to Add Parentheses][1]

[1]: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66331/C++-4ms-Recursive-and-DP-solution-with-brief-explanation