# problem
>Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
1. insert(val): Inserts an item val to the collection.
2. remove(val): Removes an item val from the collection if present.
3. getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.

Example:
```
// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
```
# codes

##  s1
```
class RandomizedCollection {
private:
    vector<int> nums;
    unordered_map<int,unordered_set<int>> m;
public:
    /** Initialize your data structure here. */
    RandomizedCollection() {
        
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        m[val].insert(nums.size());
        nums.push_back(val);
        return  m[val].size()==1;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        if(m[val].empty()){
            return false;
        }
        int idx=*m[val].begin();
        m[val].erase(idx);
        if(idx!=nums.size()-1){
            int t=nums.back();
            nums[idx]=t;
            m[t].erase(nums.size()-1);
            m[t].insert(idx);
        }
        nums.pop_back();
        return true;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        return nums[rand()%nums.size()];
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```

# analysis
- 要达到O(1)，数组+hash,hash的值存放数组的下标，这里允许重复，所以hash表的值是一个set集合，用以排序。删除的时候，我们先取出一个重复的值的索引，然后在数组的相应位置进行删除，如果是末尾，就直接删除，如果不是末尾，则需要把末尾的值搬到需要删除的位置，然后删除末尾的值。然后更新一下hash相应的索引就行了。

- 注意我们在建立哈希表的映射的时候需要用set而不是普通的vector数组，因为我们每次remove操作后都会移除nums数组的尾元素，如果我们用vector来保存数字的坐标，而且只移出末尾数字的话，有可能出现前面的坐标大小超过了此时nums的大小的情况，就会出错. 所以我们用set对所有的相同数字的坐标进行自动排序，每次把最大位置的坐标移出即可.


# reference
[[LeetCode] Insert Delete GetRandom O(1) - Duplicates allowed 常数时间内插入删除和获得随机数 - 允许重复][1]

[1]: http://www.cnblogs.com/grandyang/p/5756148.html
