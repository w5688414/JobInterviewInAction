# problem
>You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
```
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
```
Note:
1. One employee has at most one direct leader and may have several subordinates.
2. The maximum number of employees won't exceed 2000.

# codes

```
/*
// Employee info
class Employee {
public:
    // It's the unique ID of each node.
    // unique id of this employee
    int id;
    // the importance value of this employee
    int importance;
    // the id of direct subordinates
    vector<int> subordinates;
};
*/
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_set<int> s;
        unordered_map<int,Employee*> m;
        for(auto e:employees){
            m[e->id]=e;
        }
        return solve(id,m,s);
    }
    int solve(int id,unordered_map<int, Employee*>& m,unordered_set<int>& s){
        if(s.count(id)) return 0;
        s.insert(id);
        int res=m[id]->importance;
        for(int num:m[id]->subordinates){
            res+=solve(num,m,s);
        }
        return res;
    }
};
```

# analysis

题目的意思是：给定你一个数组，数组中的值依次代表雇员id，重要值，下级关系。现在要求返回给定雇员的总重要值（要求累加其雇员的重要值）。
- 一理解题意，马上就要想到是深度优先搜索。首先我们用hash表建立雇员与其下级的键值对，用集合s来标记遍历过的雇员。对遍历的每个雇员，累加其重要值和其下属的重要值。

# reference

[[LeetCode] Employee Importance 员工重要度][1]

[1]: http://www.cnblogs.com/grandyang/p/7639798.html