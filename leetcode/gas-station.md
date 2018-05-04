# problem
>There are N gas stations along a circular route, where the amount of gas at station i isgas[i].

You have a car with an unlimited gas tank and it costscost[i]of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note: 
The solution is guaranteed to be unique.

# codes

## solution 1
```
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int start=gas.size()-1;
        int end=0;
        int sum=gas[start]-cost[start];
        while(start>=end){
            if(sum>=0){
                sum+=gas[end]-cost[end];
                end++;                
            }else{
                start--;
                sum+=gas[start]-cost[start];   
            }
        }
        return sum>=0 ? start:-1;
    }
};

```

## solution 2
```
class Solution {  
public:  
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)   
    {  
        int sum = 0;  
        int total = 0;  
        int j = -1;  
        for(int i = 0; i < gas.size() ; ++i)  
        {  
            sum += gas[i]-cost[i];  
            total += gas[i]-cost[i];  
            if(sum < 0)  
            {  
                j=i; sum = 0;   
            }  
        }  
        if(total<0) return -1;  
        else return j+1;  
    }  
};
```

# analysis
>从start出发，如果油量够，可以一直向后走end++;油量不够的时候，
start向后退，最终start==end的时候，如果有解一定是当前start所在位置。

## 另一种思路
程序一：记录最后一个加起来小于零的索引，然后返回这个索引+1就是答案了。
程序二：跳跃式，跃过不能作为出发点的点，加速循环

# reference
[[编程题]gas-station][1]
[原LeetCode Gas Station 两个特性，两种方法完美解答-更新证明方法][2]

[1]: https://www.nowcoder.com/questionTerminal/3b1abd8ba2e54452b6e18b31780b3635
[2]: https://blog.csdn.net/kenden23/article/details/14106137
