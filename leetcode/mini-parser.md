# problem
>Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

- String is non-empty.
- String does not contain white spaces.
- String contains only digits 0-9, [, - ,, ].

Example 1:
```
Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
```
Example 2:
```
Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
```

# codes

```
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    NestedInteger deserialize(string s) {
        if(s.empty()){
            return NestedInteger();
        }
        if(s[0]!='[') {
            return NestedInteger(stoi(s));
        }
        if(s.size()<=2){
            return NestedInteger();
        }
        int cnt=0;
        NestedInteger res;
        int start=1;
        for(int i=1;i<s.length();i++){
            if(cnt==0&&(s[i]==','||i==s.length()-1)){
                res.add(deserialize(s.substr(start,i-start)));
                start=i+1;
            }else if(s[i]=='['){
                cnt++;
            }else if(s[i]==']'){
                cnt--;
            }
        }
        return res;
    }
};
```

# analysis
>这个递归我也写不出来。
- 首先判断s是否为空，为空直接返回，不为空的话看首字符是否为'['，不是的话说明s为一个整数，我们直接返回结果。如果首字符是'['，且s长度小于等于2，说明没有内容，直接返回结果。
- 反之如果s长度大于2，我们从i=1开始遍历，我们需要一个变量start来记录某一层的起始位置，用cnt来记录跟起始位置是否为同一深度，cnt=0表示同一深度，由于中间每段都是由逗号隔开，所以当我们判断当cnt为0，且当前字符是逗号或者已经到字符串末尾了，我们把start到当前位置之间的字符串取出来递归调用函数，把返回结果加入res中，然后start更新为i+1。如果遇到'['，计数器cnt自增1，若遇到']'，计数器cnt自减1。


# reference
[[LeetCode] Mini Parser 迷你解析器][1]
[1]: http://www.cnblogs.com/grandyang/p/5771434.html
