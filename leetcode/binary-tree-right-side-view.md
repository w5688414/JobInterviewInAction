# problem
>Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Example:
```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

# codes

## s1 bfs
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
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if(!root){
            return res;
        }
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* t;
        while(!q.empty()){
            int n=q.size();
            for(int i=0;i<n;i++){
                t=q.front();
                q.pop();
                if(t->left){
                    q.push(t->left);
                }
                if(t->right){
                    q.push(t->right);
                }
            }
            res.push_back(t->val);
        }
        return res;
    }
};
```
## s2 dfs
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
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> views;
        scan(root, 0, views);
        return views;
     }
private:
    void scan(TreeNode* root, int h, vector<int>& views)
    {
        if(!root)   return;
        if(h >= views.size())
            views.emplace_back(root->val);
        /* 先遍历右侧，这样就可以先选择右边的元素 */
        scan(root->right, h + 1, views);
        scan(root->left, h + 1, views);
    }
};
```

# analysis
 我以前只实现了BFS版本，但是好像还有DFS版本，学习了，还比较巧妙。

# reference
[每天一道LeetCode-----从右向左观察一棵二叉树，返回能看到的元素][1]

[1]: https://blog.csdn.net/sinat_35261315/article/details/79412009
