# problem
>N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?
Example 1:
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
```

Note:
1. 0 <= N <= 10 ^ 4
2. 0 < target <= 10 ^ 6
3. 0 < speed[i] <= 10 ^ 6
4. 0 <= position[i] < target
5. All initial positions are different.



# codes
```
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        map<int,double> m;
        for(int i=0;i<position.size();i++){
            m[-position[i]]=(double)(target-position[i])/speed[i];
        }
        int res=0;
        double cur=0;
        for(auto it:m){
            if(it.second>cur){
                cur=it.second;
                res++;
            }
        }
        return res;
    }
};
```

# analysis
>这个解法有点特别，我做不出来，它利用了map自身的排序的功能，然后把-positon[i]当成键，这样值越大，取负数越小，则遍历的时候就从小到大遍历，解法真牛。我验证了一下，确实是正确的。

# reference
[853. Car Fleet][1]

[1]: https://leetcode.com/problems/car-fleet/discuss/139850/C++JavaPython-Straight-Forward