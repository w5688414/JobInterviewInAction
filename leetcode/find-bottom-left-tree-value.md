# problem
>Given a binary tree, find the leftmost value in the last row of the tree.
Example 1:
```
Input:

    2
   / \
  1   3

Output:
1
```
Example 2:
```
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
```
# codes
```
class Solution {
public:
    string findReplaceString(string S, vector<int>& indexes, vector<string>& sources, vector<string>& targets) {
        vector<pair<int,int>> v;
        for(int i=0;i<indexes.size();i++){
            v.push_back(make_pair(indexes[i],i));
        }
        sort(v.rbegin(),v.rend());
        for(auto p:v){
            int i=p.first;
            string s=sources[p.second];
            string t=targets[p.second];
            if(S.substr(i,s.length())==s){
                S=S.substr(0,i)+t+S.substr(i+s.length());
            }
        }
        return S;
    }
};
```

# analysis
>这道题目从前往后替换会很麻烦，因为替换后长度发生变化；后面发现别人是从后往前替换的，真是思维巧妙，佩服佩服。

# reference
[833. Find And Replace in String][1]

[1]: https://leetcode.com/problems/find-and-replace-in-string/discuss/130587/C++JavaPython-Replace-S-from-right-to-left