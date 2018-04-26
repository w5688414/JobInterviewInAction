# problem
>Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2]have the following unique permutations:
[1,1,2],[1,2,1], and[2,1,1].

# codes

```
class Solution {
private:
    int array[19]={0};
    void permutations(vector<vector<int> > &result,vector<int> &num,int start,int n){
        if(start==n){
            result.push_back(num);
        }else{
            for(int i=0;i<19;i++){
                if(array[i]>0){
                    array[i]--;
                    num[start]=i-9;
                    permutations(result,num,start+1,n);
                    array[i]++;
                }
            }
        }
    }
public:
    vector<vector<int> > permuteUnique(vector<int> &num) {
        for(int i=0;i<num.size();i++){
            array[num[i]+9]++;
        }
        vector<vector<int> > result;
        permutations(result,num,0,num.size());
        return result;
    }
};
```
# analysis
>这道题我开始没有思路，原来还是经典的深度优先遍历的问题，这里对相同数字的处理很巧妙，是我要学习的地方。
- 特异全排列，候选为-9~9,19个数字
使用array[19]记录着19个数字在序列中出现的次数
条件 ： array 中记录 i, array[i]>0 ，就是原始序列中的这个字母还没有被用完

## reference
[[编程题]permutations-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/a43a2b986ef34843ac4fdd9159b69863
