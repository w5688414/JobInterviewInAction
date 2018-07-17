# problem
>In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:
```
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
```
Note:
1. 1 <= len(start) = len(end) <= 10000.
2. Both start and end will only consist of characters in {'L', 'R', 'X'}.

# codes
```
class Solution {
public:
    bool canTransform(string start, string end) {
        int i=0,j=0;
        int n=start.size();
        while(i<n&&j<n){
            while(i<n&&start[i]=='X') ++i;
            while(j<n&&end[j]=='X') ++j;
            if(start[i]!=end[j]) return false;
            if((i<j&&start[i]=='L')||(i>j&&start[i]=='R')){
                return false;
            }
            i++;
            j++;
        }
        return true;
    }
};
```

# analysis
>不论是L还是R，其只能跟X交换位置，L和R之间是不能改变相对顺序的，所以如果分别将start和end中所有的X去掉后的字符串不相等的话，那么就永远无法让start和end相等了。

这个判断完之后，就来验证L只能前移，R只能后移这个限制条件吧，当i指向start中的L时，那么j指向end中的L必须要在前面，所以如果i小于j的话，就不对了，同理，当i指向start中的R，那么j指向end中的R必须在后面，所以i大于j就是错的，最后别忘了i和j同时要自增1，不然死循环了。

# reference
[[LeetCode] Swap Adjacent in LR String 交换LR字符串中的相邻项][1]

[1]: http://www.cnblogs.com/grandyang/p/9001474.html