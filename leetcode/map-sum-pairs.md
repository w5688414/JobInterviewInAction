# problem
>Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
```
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
```

# codes

## s1
```
class MapSum {
private:
    map<string,int> m;
public:
    /** Initialize your data structure here. */
    MapSum() {
        
    }
    
    void insert(string key, int val) {
        m[key]=val;
    }
    
    int sum(string prefix) {
        int res=0,n=prefix.size();
        for(auto it=m.lower_bound(prefix);it!=m.end();it++){
            if(it->first.substr(0,n)!=prefix){
                break;
            }
            res+=it->second;
        }
        return res;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
```


# analysis
>在map里会按照字母顺序自动排序，然后在sum函数里，我们根据prefix来用二分查找快速定位到第一个不小于prefix的位置，然后向后遍历，向后遍历的都是以prefix为前缀的单词，如果我们发现某个单词不是以prefix为前缀了，直接break；否则就累加其val。


# reference
[[LeetCode] Map Sum Pairs 映射配对之和][1]


[1]: http://www.cnblogs.com/grandyang/p/7616525.html