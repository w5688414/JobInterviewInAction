# problem
>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
Example:
```
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
```

# codes
```
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int i=1;
        int j=n;
        while(i<j){
            int mid=i+(j-i)/2;
            if(isBadVersion(mid)){
                j=mid;
            }else{
                i=mid+1;
            }
        }
        return i;
    }
};
```

# analysis
>这里需要注意的一点是，int mid=i+(j-i)/2能够避免数据溢出的问题。

# reference
[[LeetCode] First Bad Version 第一个坏版本][1]

[1]: http://www.cnblogs.com/grandyang/p/4790469.html