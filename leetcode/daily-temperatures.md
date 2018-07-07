# problem
>Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

# codes
```
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n=temperatures.size();
        vector<int> res(n,0);
        stack<int> st;
        for(int i=0;i<n;i++){
            while(!st.empty()&&temperatures[i]>temperatures[st.top()]){
                int t=st.top();
                st.pop();
                res[t]=i-t;
            }
            st.push(i);
        }
        return res;
    }
};
```

# analysis
>这里用了栈的方法，巧妙的解决了差值的问题，斩里面存放的是递减的温度值的索引。这个题目跟那个柱形图装水很像。

# reference
[[LeetCode] Daily Temperatures 日常温度][1]

[1]: http://www.cnblogs.com/grandyang/p/8097513.html