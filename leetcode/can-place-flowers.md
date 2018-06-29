# problem
>Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
```
Example 2:
```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
```
Note:
1. The input array won't violate no-adjacent-flowers rule.
2. The input array size is in the range of [1, 20000].
3. n is a non-negative integer which won't exceed the input array size.

# codes
```
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int m=flowerbed.size();
        int i=0;
        int cnt=0;
        while(i<m){
            if(flowerbed[i]==1){
                i+=2;
            }else if(i+1<m&&flowerbed[i+1]==0){
                cnt++;
                i+=2;
            }else if(i==m-1&&flowerbed[i-1]==0){
                cnt++;
                break;
            }else{
                i++;
            }
        }
        return cnt>=n;
    }
};
```

# analysis
>这道题还有一个解法在参考文献里面，上面的解法是我自己想出来的，后面我有时间就实现一下下面的方法。

# reference
[[LeetCode] Can Place Flowers 可以放置花][1]


[1]: http://www.cnblogs.com/grandyang/p/6983982.html
