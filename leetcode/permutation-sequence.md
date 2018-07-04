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

## s1
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
## s2
```
class Solution {
public:
    string getPermutation(int n, int k) {
       string res;
        string num="123456789";
        vector<int> v(n,1);
        for(int i=1;i<n;i++){
            v[i]=v[i-1]*i;
        }
        k--;
        for(int i=n;i>=1;i--){
            int j=k/v[i-1];
            k=k%v[i-1];
            res.push_back(num[j]);
            num.erase(j,1);
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

## s2
看k = 17这种情况的每位数字如何确定，由于k = 17是转化为数组下标为16：

最高位可取1,2,3,4中的一个，每个数字出现3！= 6次，所以k = 16的第一位数字的下标为16 / 6 = 2，即3被取出
第二位此时从1,2,4中取一个，k = 16是此时的k' = 16 % (3!) = 4，而剩下的每个数字出现2！= 2次，所以第二数字的下标为4 / 2 = 2，即4被取出
第三位此时从1,2中去一个，k' = 4是此时的k'' = 4 % (2!) = 0，而剩下的每个数字出现1！= 1次，所以第三个数字的下标为 0 / 1 = 0，即1被取出
第四位是从2中取一个，k'' = 0是此时的k''' = 0 % (1!) = 0，而剩下的每个数字出现0！= 1次，所以第四个数字的下标为0 / 1= 0，即2被取出

那么我们就可以找出规律了
a1 = k / (n - 1)!
k1 = k

a2 = k1 / (n - 2)!
k2 = k1 % (n - 2)!
...

an-1 = kn-2 / 1!
kn-1 = kn-2 / 1!

an = kn-1 / 0!
kn = kn-1 % 0!

## reference
[[编程题]permutation-sequence][1]
[[LeetCode] Permutation Sequence 序列排序][2]
[Leetcode #60. Permutation Sequence 排列组合序列 解题报告][1]

[1]: https://www.nowcoder.com/questionTerminal/186c35e87f7b45beaa556dbbf670759e
[2]: https://www.cnblogs.com/grandyang/p/4358678.html
[3]: https://blog.csdn.net/MebiuW/article/details/51288495