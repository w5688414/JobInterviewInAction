# problem
>You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time .

Given an integer array representing the number of dresses in each washing machine from left to right on the line, you should find the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.

Example 1:
```
Input: [1,0,5]

Output: 3

Explanation: 
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
3rd move:    2     1 <-- 3    =>    2     2     2 
```
Example 2:
```
Input: [0,3,0]

Output: 2

Explanation: 
1st move:    0 <-- 3     0    =>    1     2     0    
2nd move:    1     2 --> 0    =>    1     1     1     
```
Example 3:
```
Input: [0,2,0]

Output: -1

Explanation: 
It's impossible to make all the three washing machines have the same number of dresses. 
```
Note:
1. The range of n is [1, 10000].
2. The range of dresses number in a super washing machine is [0, 1e5].

# codes
```
class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        int n=machines.size();
        int sum=0;
        for(int num:machines){
            sum+=num;
        }
        if(sum%n!=0){
            return -1;
        }
        int res=0;
        int avg=sum/n;
        int cnt=0;
        for(int m:machines){
            cnt+=m-avg;
            res=max(res,max(abs(cnt),m-avg));
        }
        return res;
    }
};
```

# analysis
>有四个洗衣机，装的衣服数为[0, 0, 11, 5]，最终的状态会变为[4, 4, 4, 4]，那么我们将二者做差，得到[-4, -4, 7, 1]，这里负数表示当前洗衣机还需要的衣服数，正数表示当前洗衣机多余的衣服数。我们要做的是要将这个差值数组每一项都变为0，对于第一个洗衣机来说，需要四件衣服可以从第二个洗衣机获得，那么就可以把-4移给二号洗衣机，那么差值数组变为[0, -8, 7, 1]，此时二号洗衣机需要八件衣服，那么至少需要移动8次。
- 然后二号洗衣机把这八件衣服从三号洗衣机处获得，那么差值数组变为[0, 0, -1, 1]，此时三号洗衣机还缺1件，就从四号洗衣机处获得，此时差值数组成功变为了[0, 0, 0, 0]，成功。那么移动的最大次数就是差值数组中出现的绝对值最大的数字，8次

我也解释不了这个，参见参考2，里面讲得还不错：

- 对位置k上的洗衣机来说，如果左边k个洗衣机中（下标从0开始）原有衣服总数小于avg*k，表明左边k个洗衣机作为整体最终需要从右边洗衣机（包含位置k）中获取衣服，而获取衣服必定需要通过位置k的洗衣机，右边同理。这里拿lCnt表示位置k左边所有洗衣机最终向右边洗衣机（包含位置k）输送的衣服数，如果lCnt小于0，表示左边洗衣机最终需要从右边洗衣机中获取衣服，同理拿rCnt表示位置k右边所有洗衣机最终向左边洗衣机（包含位置k）中输送的衣服数。lCnt和rCnt在知道了avg之后很容易计算，这样通过判断lCnt和rCnt的正负即可得出位置k上洗衣机的最小操作数。

- 如果lCnt>0 && rCnt>0
​表明位置k需要同时从两侧获取衣服，两侧可以同时进行，所以位置k上最小操作数为max(lCnt, rCnt)；
- 如果lCnt<0 && rCnt<0
表明位置k同时向两侧输出衣服，两侧不能同时进行，所以位置k上最小操作数为-lCnt-rCnt；
- 其他情况
- 表明位置k需要从一侧获取衣服，然后向另一侧输出衣服，两侧可以同时进行，所以位置k上最小操作数为max(abs(lCnt), abs(rCnt))。

# reference
[[LeetCode] Super Washing Machines 超级洗衣机][1]
[[leetcode] 517. Super Washing Machines][2]
[517. Super Washing Machines][3]

[1]: http://www.cnblogs.com/grandyang/p/6648557.html
[2]: https://blog.csdn.net/TstsUgeg/article/details/62427718
[3]: https://leetcode.com/problems/super-washing-machines/discuss/99185/super-short-easy-java-on-solution