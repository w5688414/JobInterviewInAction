# problem
> In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.
```
Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
```
Note:

1. answers will have length at most 1000.
2. Each answers[i] will be an integer in the range [0, 999].

# codes
```
class Solution {
public:
    int numRabbits(vector<int>& answers) {
        int res=0;
        unordered_map<int,int> m;
        for(int i=0;i<answers.size();i++){
            if(!m[answers[i]+1]){
                res+=answers[i]+1;
                m[answers[i]+1]=answers[i];
            }else{
                m[answers[i]+1]--;
            }
        }
        return res;
    }
};
```

# analysis
>这道题目我也做不出来，这个规律太难找了，直接蒙圈。

- 例如[0, 0, 1, 1, 1]，前两只兔子都说森林里没有兔子和其颜色相同了，那么这两只兔子就是森林里独一无二的兔子，且颜色并不相同，所以目前已经确定了两只。
- 然后后面三只都说森林里还有一只兔子和其颜色相同，那么这三只兔子就不可能颜色都相同了，但我们可以让两只颜色相同，另外一只颜色不同，那么就是说还有一只兔子并没有在数组中，所以森林中最少有6只兔子。
- 分析完了这几个例子，我们可以发现，如果某个兔子回答的数字是x，那么说明森林里共有x+1个相同颜色的兔子，我们最多允许x+1个兔子同时回答x个，一旦超过了x+1个兔子，那么就得再增加了x+1个新兔子了。
- 所以我们可以使用一个HashMap来建立某种颜色兔子的总个数和在数组中还允许出现的个数之间的映射，然后我们遍历数组中的每个兔子，如果该兔子回答了x个，若该颜色兔子的总个数x+1不在HashMap中，或者映射为0了，我们将这x+1个兔子加入结果res中，然后将其映射值设为x，表示在数组中还允许出现x个也回答x的兔子；否则的话，将映射值自减1即可

# reference
[[LeetCode] Rabbits in Forest 森林里的兔子][1]


[1]: http://www.cnblogs.com/grandyang/p/9043761.html