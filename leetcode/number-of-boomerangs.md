# problem
>Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
```
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
```


# codes

## s1
```
class Solution {
public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        int res=0;
        for(int i=0;i<points.size();i++){
            unordered_map<int,int> m;
            for(int j=0;j<points.size();j++){
                int a=points[j].first-points[i].first;
                int b=points[j].second-points[i].second;
                m[a*a+b*b]++;
            }
            for(auto t:m){
                res+=t.second*(t.second-1);
            }
        }
        return res;
    }
};
```

# analysis
>如果我们有一个点a，还有两个点b和c，如果ab和ac之间的距离相等，那么就有两种排列方法abc和acb；如果有三个点b，c，d都分别和a之间的距离相等，那么有六种排列方法，abc, acb, acd, adc, abd, adb，类推：如果有n个点，那么排列方式为n*(n-1)
- 那么我们问题就变成了遍历所有点，让每个点都做一次点a，然后遍历其他所有点，统计和a距离相等的点有多少个，然后分别带入n(n-1)计算结果并累加到res中，只有当n大于等于2时，res值才会真正增加

# reference
[[LeetCode] Number of Boomerangs 回旋镖的数量][1]

[1]: http://www.cnblogs.com/grandyang/p/6049382.html