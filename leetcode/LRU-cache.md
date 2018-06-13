# problem
>Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Follow up:
Could you do both operations in O(1) time complexity?
Example:
```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

# codes
```
class LRUCache {
private:
    list<pair<int,int>> cache;
    int size;
    unordered_map<int,list<pair<int,int>>::iterator> hash;
public:
    LRUCache(int capacity) {
        size=capacity;
    }
    
    int get(int key) {
        auto it=hash.find(key);
        if(it==hash.end()) return -1;
        cache.splice(cache.begin(),cache,it->second);
        return it->second->second;
    }
    
    void put(int key, int value) {
        auto it=hash.find(key);
        if(it!=hash.end()){
            it->second->second=value;
            cache.splice(cache.begin(),cache,it->second);
            return;
        }
        cache.insert(cache.begin(),make_pair(key,value));
        hash[key]=cache.begin();
        if(cache.size()>size){
            hash.erase(cache.back().first);
            cache.pop_back();
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

# analysis
>如果来了一个get请求, 我们仍然先去查hash表, 如果key存在hash表中, 那么需要将这个结点在链表的中的位置移动到链表首部.否则返回-1.
另外一个非常关键的降低时间复杂度的方法是在hash中保存那个key在链表中对应的指针, 我们知道链表要查找一个结点的时间复杂度是O(n), 所以当我们需要移动一个结点到链表首部的时候, 如果直接在链表中查询那个key所对于的结点, 然后再移动, 这样时间复杂度将会是O(n), 而一个很好的改进方法是在hash表中存储那个key在链表中结点的指针, 这样就可以在O(1)的时间内移动结点到链表首部.

STL技巧：
1、使用map的find方法来判断key是否已经存在,返回值和map的end迭代器比较； 
2、使用unordered_map,它是hash_map,存取时间都是O(1),用它存储元素的position迭代器,是为了方便splice函数调用list.splice(position, list, element_pos)函数作用是把list的element_pos处的元素插入到position位置,本题中为了移动元素到list头部

思路都显而易见，但是还是写不出来，C++的这几个函数不会，妈蛋。

# reference
[[leetcode] 146. LRU Cache 解题报告][1]


[1]: https://blog.csdn.net/qq508618087/article/details/50995188


