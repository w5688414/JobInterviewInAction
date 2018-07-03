# problem
> Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code. This represents the result of splitting the original source code string by the newline character \n.

In C++, there are two types of comments, line comments, and block comments.

The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.

The string /* denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.

The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters. For example, source = "string s = "/* Not a comment. */";" will not be a test case. (Also, nothing else such as defines or macros will interfere with the comments.)

It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.
Example 1:
```
Input: 
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}

Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{ 
  
int a, b, c;
a = b + c;
}

Explanation: 
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
Example 2:
Input: 
source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
```

Note:
- The length of source is in the range [1, 100].
- The length of source[i] is in the range [0, 80].
- Every open block comment is eventually closed.
- There are no single-quote, double-quote, or control characters in the source code.

# codes
```
class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        vector<string> res;
        bool blocked=false;
        string out="";
        int n=source.size();
        for(string line:source){
            for(int i=0;i<line.size();i++){
                if(!blocked){
                   if(i==line.length()-1){
                        out+=line[i];
                    }else{
                        string t=line.substr(i,2);
                        if(t=="/*"){
                            blocked=true;
                            i++;
                        }else if(t=="//"){
                            break;
                        }else{
                            out+=line[i];
                        }
                    } 
                }else{
                    if(i<line.size()-1){
                        string t=line.substr(i,2);
                        if(t=="*/"){
                            blocked=false;
                            i++;
                        }
                    }
                }
                
            }
            if(!out.empty()&&!blocked){
                res.push_back(out);
                out="";
            }
        }
        return res;
    }
};
```

# analysis
> 我们需要一个变量blocked来记录当前是否为块注释状态，初始化为false。建立空字符out，用来保存去除注释后的字符。然后我们遍历整个代码的每一行，遍历每一行中的每一个字符，如果当前字符是最后一个字符了，说明不会再有注释了，将当前字符加入out中，否则取出当前位置和下一个位置的两个字符，如果其正好是"/*"，说明之后的部分都是块注释了，我们将blocked赋值为true，然后指针向后移动一个，明明两个字符啊，为啥只移动一个呢，因为另一个可以在for循环中的++i移动；如果当前两个字符正好是"//"，说明当前行之后都是注释，我们并不care后面有啥，所以可以直接break掉当前行；如果都不是，说明当前字符是代码，将其加入out中。
- 来看blocked为true的情况，说明之后的内容都是块注释的内容，我们唯一关心的是有没有结束符"*/"，所以还是先做判断，如果当前不是最后一个字符，说明至少还有两个字符，然后取出两个字符，如果正好是块注释结束符，那么我们将标识重置为false，指针要后移动一个。当前行遍历完后，如果out不为空，且blocked为false，则将out存入结果res中

# reference
[[LeetCode] Remove Comments 移除注释][1]

[1]: http://www.cnblogs.com/grandyang/p/7841824.html