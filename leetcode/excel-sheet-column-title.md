# problem
>Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```
Example 1:
```
Input: 1
Output: "A"
```
Example 2:
```
Input: 28
Output: "AB"
```
Example 3:
```
Input: 701
Output: "ZY"
```

# codes
## s1
```
class Solution {
public:
    string convertToTitle(int n) {
        string res;
        while(n){
            if(n%26==0){
                res.push_back('Z');
                n=n/26;
                n--;
                if(!n){
                    break;
                }
            }else{
               res.push_back(n%26+'A'-1); 
                n=n/26;
            }

        }
        
        reverse(res.begin(),res.end());
        return res;
    }
};
```
## r1
```
   std::string str( "" );
    while( n  )
    {
        str = char( ( n - 1 ) % 26 + 'A') + str;
        n = ( n  - 1 )/26;            
    }
    return str;
    
}
```

# analysis
>我想到了n+1，却没有想到n-1，看来还是要历练，s1是我的解法，有点复杂。
 
# reference
[168. Excel Sheet Column Title][1]

[1]: https://leetcode.com/problems/excel-sheet-column-title/discuss/139286/C++-Iterative-Simple