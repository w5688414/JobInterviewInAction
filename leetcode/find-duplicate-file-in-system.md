# problem
>
Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"
Example 1:
```
Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

```
Note:
1. No order is required for the final output.
2. You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].
3. The number of files given is in the range of [1,20000].
4. You may assume no files or directories share the same name in the same directory.
5. You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.

Follow-up beyond contest:
1. Imagine you are given a real file system, how will you search files? DFS or BFS?
2. If the file content is very large (GB level), how will you modify your solution?
3. If you can only read the file by 1kb each time, how will you modify your solution?
4. What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
5. How to make sure the duplicated files you find are not false positive?

# codes
```
class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        vector<vector<string>> res;
        unordered_map<string,vector<string>> m;
        for(string path:paths){
            istringstream is(path);
            string pre="",t="";
            is>>pre;
            while(is>>t){
                int idx=t.find_last_of('(');
                string dir=pre+"/"+t.substr(0,idx);
                string content=t.substr(idx+1,t.size()-1-(idx+1));
                m[content].push_back(dir);
            }
        }
        for(auto a:m){
            if(a.second.size()>1){
                res.push_back(a.second);
            }
        }
        return res;
    }
};
```

# analysis
>这道题用java或者python我都会做，但是用c++，我感觉对我还是有难度的，毕竟istringstream不会用。anyway 我copy下来了，学习一下。

# reference
[[LeetCode] Find Duplicate File in System 在系统中寻找重复文件][1]

[1]: http://www.cnblogs.com/grandyang/p/7007974.html