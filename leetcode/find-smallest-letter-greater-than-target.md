# problem
>Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
```
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
```

Note:
1. letters has a length in range [2, 10000].
2. letters consists of lowercase letters, and contains at least 2 unique letters.
3. target is a lowercase letter.

# codes
```
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        if (target >= letters.back()) return letters[0];
        int i=0;
        int j=letters.size()-1;
        int n=letters.size();
        while(i<j){
            int mid=i+(j-i)/2;
            if(letters[mid]<=target){
                i=mid+1;
            }else{
                j=mid;
            }
        }
        return letters[j];
    }
};
```

# analysis
>二分法，这里注意判断条件需要变一下，不然带有重复字符的二分法通过不了。
# reference
[LeetCode Binary Search Summary 二分搜索法小结][1]
[[LeetCode] Find Smallest Letter Greater Than Target 找比目标值大的最小字母][2]

[1]: http://www.cnblogs.com/grandyang/p/6854825.html
[2]: http://www.cnblogs.com/grandyang/p/8284940.html