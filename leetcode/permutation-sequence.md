# problem
>The set[1,2,3,…,n]contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the k th permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

# codes

```
class Solution {
private:
    int count=0;
    string result;
    vector<int> v1;
    int book[15] = {0};
public:
    string getPermutation(int n, int k) {
        Permutation(n,0,k);
        return result;
    }
    void Permutation(int n,int start,int k){
        if(start==n){
            count++;
            if(count==k){
                for(int i=0;i<v1.size();i++){
                    char ch=v1[i]+'0';
                    result=result+ch;
                }
                return;
            }
        }else{
            for(int i=1;i<=n;i++){
                if(book[i]==0){
                    v1.push_back(i);
                    book[i]=1;
                    Permutation(n,start+1,k);
                    book[i]=0;
                    v1.pop_back();                
                }
            }            
        }

    }
};

```
```
class Solution {
public:
    string getPermutation(int n, int k) {
        string res;
        string num = "123456789";
        vector<int> f(n, 1);
        for (int i = 1; i < n; ++i) f[i] = f[i - 1] * i;
        --k;
        for (int i = n; i >= 1; --i) {
            int j = k / f[i - 1];
            k %= f[i - 1];
            res.push_back(num[j]);
            num.erase(j, 1);
        }
        return res;
    }
};
```
# analysis
>这里用了深度优先搜索，然后加入了book数组，来记录深度遍历的时候，1～n中的某个元素是否已经用过。当然也有更好的办法，我等会儿来完善一下。
>最优的解法不是这个，这个算法理解起来有点麻烦，我这里举一个例子。
假设集合为[1,2,3,4]，求出第6个组合。 
第6个组合对应的下标为5（下标从0开始），我们首先求出5所对应的lehmer码（lehmer code的解释参考链接1）： 
5/3! = 0 余5 
5/2! = 2 余1 
1/1! = 1 余0 
0 (lehmer code最后一位总为0) 
所以所求lehmer码为0210

当前集合对应的序列为1234 
接下来将lehmer码中的每个数字当做当前序列的下标，下标0对应的集合元素为1，当前序列变成234；下标2对应的集合元素为4，当前序列变成23；下标1对应的集合元素为3，当前序列变成2；下标0对应的元素为2 
所以所求的组合即为1432

## reference
[[编程题]permutation-sequence][1]
[[LeetCode] Permutation Sequence 序列排序][2]
[Leetcode #60. Permutation Sequence 排列组合序列 解题报告][1]

[1]: https://www.nowcoder.com/questionTerminal/186c35e87f7b45beaa556dbbf670759e
[2]: https://www.cnblogs.com/grandyang/p/4358678.html
[3]: https://blog.csdn.net/MebiuW/article/details/51288495