# problem
>Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

For example,
If S =[1,2,2], a solution is:
```
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```
# codes
## s1
```
class Solution {
private:
    vector<vector<int> > result;
    vector<int> ans;
public:
    vector<vector<int> > subsetsWithDup(vector<int> &S) {
        sort(S.begin(),S.end());
        dfs(S,0);
        return result;
    }
    void dfs(vector<int> S,int start){
        result.push_back(ans);
        for(int i=start;i<S.size();i++){
            ans.push_back(S[i]);
            dfs(S,i+1);
            while(i<S.size()-1&&S[i+1]==S[i]){
                ++i;
            }
            ans.pop_back();
        }
    }
};

```
## s2
```
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        if(nums.empty()){
            return {};
        }
        sort(nums.begin(),nums.end());
        vector<vector<int>> res(1);
        int last=nums[0];
        int size=1;
        for(int i=0;i<nums.size();i++){
            if(last!=nums[i]){
                last=nums[i];
                size=res.size();
            }
            int newSize=res.size();
            for(int j=newSize-size;j<newSize;j++){
                res.push_back(res[j]);
                res.back().push_back(nums[i]);
            }
        }
        return res;
    }
};
```

# analysis
>看完了思路还是蛮简单的，就是一个深度优先搜索，先对vector进行排序，如果在遍历的时候，遇见重复的，则需要跳过去。

## s2
这是一个非递归的写法。
拿题目中的例子[1 2 2]来分析，根据之前 Subsets 子集合 里的分析可知，当处理到第一个2时，此时的子集合为[], [1], [2], [1, 2]，而这时再处理第二个2时，如果在[]和[1]后直接加2会产生重复，所以只能在上一个循环生成的后两个子集合后面加2，发现了这一点，题目就可以做了，我们用last来记录上一个处理的数字，然后判定当前的数字和上面的是否相同，若不同，则循环还是从0到当前子集的个数，若相同，则新子集个数减去之前循环时子集的个数当做起点来循环，这样就不会产生重复了。

# reference
[[编程题]subsets-ii][1]
[[LeetCode] Subsets II 子集合之二][2]

[1]: https://www.nowcoder.com/questionTerminal/66cf0498e9fd4730ab453dac978bf7e6
[2]: http://www.cnblogs.com/grandyang/p/4310964.html