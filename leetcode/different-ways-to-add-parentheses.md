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
>这还不是最好的方案，明天再看吧，现在有点晚了。

# reference

[241. Different Ways to Add Parentheses][1]

[1]: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66331/C++-4ms-Recursive-and-DP-solution-with-brief-explanation