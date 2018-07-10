# problem
>We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:
```
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
```
Notes:

1. 1 <= difficulty.length = profit.length <= 10000
2. 1 <= worker.length <= 10000
3. difficulty[i], profit[i], worker[i]  are in range [1, 10^5]

# codes
```
class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int,int>> jobs;
        int n=profit.size();
        int res=0;
        for(int j=0;j<n;j++){
            jobs.push_back({difficulty[j],profit[j]});
        }
        sort(jobs.begin(),jobs.end());
        sort(worker.begin(),worker.end());
        int i=0;
        int mx=0;
        for(int ability:worker){
            while(i<n&&ability>=jobs[i].first){
               mx=max(mx,jobs[i].second);
                i++;
            }
            res+=mx;
        }
        return res;
    }
};
```

# analysis
>先进行排序，然后一个一个的找到其最大profit就行了，如果没有想到用vector pair进行排序，可能就做不出来了。
时间复杂度: O(NlogN+QlogQ)
空间复杂度: O(N)

# reference
[826. Most Profit Assigning Work][1]

[1]: https://leetcode.com/problems/most-profit-assigning-work/discuss/127031/C++JavaPython-Sort-and-Two-pointer