# problem
>Clone an undirected graph. Each node in the graph contains alabeland a list of itsneighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use#as a separator for each node, and,as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph{0,1,2# 1,2# 2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by#.

First node is labeled as0. Connect node0to both nodes1and2.
Second node is labeled as1. Connect node1to node2.
Third node is labeled as2. Connect node2to node2(itself), thus forming a self-cycle.

Visually, the graph looks like the following:
```
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
```
# codes
## s1
```
/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        // 拷贝所有节点, BFS, 并建立一个新节点地址与老节点地址的对应关系
        map<UndirectedGraphNode *, UndirectedGraphNode *> mymap;
        BFS(node,mymap);
        // 更新新节点内部的指针数组
        for(map<UndirectedGraphNode *, UndirectedGraphNode *>::iterator iter=mymap.begin();
           iter!=mymap.end();iter++){
            for(int i=0;i<(iter->first)->neighbors.size();i++){
                UndirectedGraphNode * temp=iter->first->neighbors[i];
                iter->second->neighbors.push_back(mymap[temp]);
            }
            
        }
        return mymap[node];
        
    }
private:
    void BFS(UndirectedGraphNode * node, map<UndirectedGraphNode *, UndirectedGraphNode *> & mymap){
        // 节点无效， 或者节点已经被访问过了
        if(node==NULL||mymap.find(node)!=mymap.end()){
            return ;
        }
        // 插入根节点位置
        queue<UndirectedGraphNode *> queue1;
        queue1.push(node);
        while(!queue1.empty()){
            // 访问队列中的节点
            UndirectedGraphNode *front=queue1.front();
            queue1.pop();
            UndirectedGraphNode *newNode=new UndirectedGraphNode(front->label);
            mymap.insert(make_pair(front,newNode));
            // 更新队列
            for(int i=0;i<front->neighbors.size();i++){
                if(mymap.find(front->neighbors[i])==mymap.end()){
                    queue1.push(front->neighbors[i]);
                }
            }
        }
    }
};

```
## s2
```
/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        unordered_map<int, UndirectedGraphNode*> umap;
        return clone(node,umap);
    }
    UndirectedGraphNode *clone(UndirectedGraphNode *node,unordered_map<int, UndirectedGraphNode*>& umap){
        if(!node) return NULL;
        if(umap.count(node->label)) return umap[node->label];
        
        UndirectedGraphNode *newNode=new UndirectedGraphNode(node->label);
        umap[node->label]=newNode;
        for(int i=0;i<node->neighbors.size();i++){
            (newNode->neighbors).push_back(clone(node->neighbors[i],umap));
        }
        return newNode;
    }
};
```

# analysis
## s1
BFS,map；我们先把所有的结点复制一遍，用一个map存储，键为老结点，值为新来的结点。然后宽度遍历其邻居结点，加入队列，加入队列前要判断map是否有重复，重复的忽略。然后我们遍历这个map，有相同的键值
## s2
这个解法是DFS的版本，相比于BFS，DFS更简洁一点。

# reference
[LeetCode 133. Clone Graph][1]

[1]: https://blog.csdn.net/zhyh1435589631/article/details/50971495