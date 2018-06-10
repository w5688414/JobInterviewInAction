# problem
>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Example:

```
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
```


# codes
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream out;
        serialize(root,out);
        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream in(data);
        return deserialize(in);
    }
private:
    void serialize(TreeNode* root,ostringstream &out){
        if(root){
            out<<root->val<<' ';
            serialize(root->left,out);
            serialize(root->right,out);
        }else{
            out<<"# ";
        }
    }
    TreeNode*  deserialize(istringstream &in){
        string val;
        in>>val;
        if(val=="#") return nullptr;
        TreeNode* root=new TreeNode(stoi(val));
        root->left=deserialize(in);
        root->right=deserialize(in);
        return root;
    }
    
    
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```

# analysis
>这是一个序列化与反序列的hard类型的题目，本质上是一个先序遍历的过程。我当时没有用stream这种函数，所以序列化处理起来就麻烦多了，这里序列化用了stream 用“ ”分隔，如果叶子结点为空，就用#来代替，这样方便在反序列化的时候找到每个数字，并且可以方便的用stoi来转换成int类型的val。

# reference
[297. Serialize and Deserialize Binary Tree][1]
[[LeetCode] Serialize and Deserialize Binary Tree 二叉树的序列化和去序列化][2]

[1]: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/132457/C++-stream-solution
[2]: https://www.cnblogs.com/grandyang/p/4913869.html

