# problem
>We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
```
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
```
Example 2:
```
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
```
Example 3:
```
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
```
Example 4:
```
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
```
Note:

- The length of asteroids will be at most 10000.
- Each asteroid will be a non-zero integer in the range [-1000, 1000]..

# codes
```
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> res;
        for(int i=0;i<asteroids.size();i++){
            if(asteroids[i]>0){
                res.push_back(asteroids[i]);
            }else if(res.empty()||res.back()<0){
                res.push_back(asteroids[i]);
            }else if(res.back()<=-asteroids[i]){
                if(res.back()<-asteroids[i]){
                    i--;
                }
                res.pop_back();
            }
        }
        return res;
    }
};
```

# analysis

题目的意思是：
意思是+代表向右，-代表向左，数组的每个值代表小行星的大小，如果两个行星相撞，小的行星会爆炸；如果两个行星大小一样，则都会爆炸，问最后剩下的行星有哪些。

解题思路：
在遍历数组的时候，
- 如果当前数字是正数的话，我们直接加入结果res；否则我们遇到的都是负数，
- 如果结果res为空，或者结果res的最后一个数字小于0（此时两个行星同时向左运动），直接将当前数字加入结果res
- 如果结果res的最后一个数字（此时为正数）小于当前数字的绝对值，说明碰撞后消失了，那么我们将i自减一个，然后将res最后一个数字移除，这样下次遍历的时候还是这个质量大的行星。如果两个质量相等，那么直接移除res最后一个数字，此时两个行星都消失了.

# reference
[[LeetCode] Asteroid Collision 行星碰撞][1]

[1]: http://www.cnblogs.com/grandyang/p/8035551.html