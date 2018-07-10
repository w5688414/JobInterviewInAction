# problem
> We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
```
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
```
Example 2:
```
Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
```
Note:
1. bottom will be a string with length in range [2, 8].
2. allowed will have length in range [0, 200].
3. Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.

# codes
```
class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        unordered_map<string,unordered_set<char>> m;
        for(string word:allowed){
            m[word.substr(0,2)].insert(word[2]);
        }
        return solve(bottom,"",m);
    }
    bool solve(string cur,string above,unordered_map<string,unordered_set<char>>& m){
        if(cur.size()==2&&above.size()==1) return true;  //1.1
        if(above.size()==cur.size()-1) return solve(above,"",m); //1.2
        int pos=above.size();
        string base=cur.substr(pos,2); //1.3
        if(m.count(base)){
            for(char ch:m[base]){
                if(solve(cur,above+string(1,ch),m)){
                    return true;
                }
            }
        }
        return false;
    }
};
```

# analysis
>这道题虽然题目看懂了，但是我不会，看来我的分析能力需要加强。
- 首先由于我们想快速知道两个字母上方可以放的字母，需要建立基座字符串和上方字符集合之间的映射，由于上方字符可以不唯一，所以用个HashSet来放字符。
1.1 我们的递归函数有三个参数，当前层字符串cur，上层字符串above，还有我们的HashMap。如果cur的大小为2，above的大小为1，那么说明当前已经达到金字塔的顶端了，已经搭出来了，直接返回true。
1.2 否则看，如果上一层的长度比当前层的长度正好小一个，说明上一层也搭好了，我们现在去搭上上层，于是调用递归函数，将above当作当前层，空字符串为上一层，将调用的递归函数结果直接返回。
1.3 否则表示我们还需要继续去搭above层，我们先算出above层的长度pos，然后从当前层的pos位置开始取两个字符，就是above层接下来需要搭的字符的基座字符。
举个例子如下：

  D   
 / \ / \
A   B   C
我们看到现在above层只有一个D，那么pos为1，在cur层1位置开始取两个字符，得到"BC"，即是D的下一个位置的字符的基座字符串base。取出了base后，如果HashMap中有映射，则我们遍历其映射的字符集合中的所有字符，对每个字符都调用递归函数，此时above字符串需要加上这个遍历到的字符，因为我们在尝试填充这个位置，如果有返回true的，那么当前递归函数就返回true了，否则最终返回false，

# reference
[[LeetCode] Pyramid Transition Matrix 金字塔转变矩阵][1]

[1]: http://www.cnblogs.com/grandyang/p/8476646.html