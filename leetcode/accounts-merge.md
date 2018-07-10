# problem
> Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
```
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
```
Note:

- The length of accounts will be in the range [1, 1000].
- The length of accounts[i] will be in the range [1, 10].
- The length of accounts[i][j] will be in the range [1, 30].

# codes

## solution 1
```
class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        vector<vector<string>> res;
        unordered_map<string,string> root; // map from an 邮箱 to its 邮箱的父亲 
        unordered_map<string,string> owner; // map from the 邮箱 to 名字  
        unordered_map<string,set<string>> m; // the unions of accounts  并查集string下的结点们
        for(auto account:accounts){
            for(int i=1;i<account.size();i++){
                root[account[i]]=account[i]; // the unions of accounts  并查集string下的结点们
                owner[account[i]]=account[0];
            }
        }
        for(auto account:accounts){
            string t=find(account[1],root);   // find and union 查找与合并 
            for(int i=2;i<account.size();i++){
                root[find(account[i],root)]=t;
            }
        }
        for(auto account:accounts){
            for(int i=1;i<account.size();i++){  //将每个邮箱结点放入它的根节点带领的并查集中
                m[find(account[i],root)].insert(account[i]);
            }
        }
        for(auto a:m){  //取出每一个map对
            vector<string> v(a.second.begin(),a.second.end());
            v.insert(v.begin(),owner[a.first]); //v.begin()前面插入owner[p.first]元素
            res.push_back(v);
        }
        return res;
    }
    string find(string s,unordered_map<string,string>& root ){
        return root[s]==s ? s:find(root[s],root);
    }
};
```

# analysis
>首先我们遍历每个账户和其中的所有邮箱，先将每个邮箱的root映射为其自身，然后将owner赋值为用户名。然后开始另一个循环，遍历每一个账号，首先对帐号的第一个邮箱调用find函数，得到其父串p，然后遍历之后的邮箱，对每个遍历到的邮箱先调用find函数，将其父串的root值赋值为p，这样做相当于将相同账号内的所有邮箱都链接起来了。我们下来要做的就是再次遍历每个账户内的所有邮箱，先对该邮箱调用find函数，找到父串，然后将该邮箱加入该父串映射的集合汇总，这样就我们就完成了合并。最后只需要将集合转为字符串数组，加入结果res中，通过owner映射找到父串的用户名，加入字符串数组的首位置.

# reference
[[LeetCode] Accounts Merge 账户合并][1]
[leetcode721——Accounts Merge][2]

[1]: http://www.cnblogs.com/grandyang/p/7829169.html
[2]: https://blog.csdn.net/tzyshiwolaogongya/article/details/79586900