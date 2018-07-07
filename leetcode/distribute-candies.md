# problem
>Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.
Example 1:
```
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 
```
Example 2:
```
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 
```
Note:

1. The length of the given array is in range [2, 10,000], and will be even.
2. The number in given array is in range [-100,000, 100,000].

# codes

```
class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        unordered_set<int> s;
        int cnt=0;
        for(int candy:candies){
            s.insert(candy);
            cnt++;
        }
        return min((int)s.size(),cnt/2); 
    }
};
```

# analysis
>由于每个人都要分一半，所以种类数不可能超过糖总数的1/2，然后我们再看糖果的种类数，每个人拿到的糖果最大种类数不可能超过现有的糖果的种类数，所以这两者取最小值就是答案。

这个我做不出来，可能现在水平不怎么够。

# reference

[[LeetCode] Distribute Candies 分糖果][1]


[1]: http://www.cnblogs.com/grandyang/p/6847675.html