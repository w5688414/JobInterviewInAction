# problem
>Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

1. postTweet(userId, tweetId): Compose a new tweet.
2. getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
3. follow(followerId, followeeId): Follower follows a followee.
4. unfollow(followerId, followeeId): Follower unfollows a followee.

Example:
```
Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
```
# codes

```
class Twitter {
private:
    int cnt=0;
    unordered_map<int,set<int>> friends;
    unordered_map<int,map<int,int>> tweets;
    
public:
    /** Initialize your data structure here. */
    Twitter() {
        
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        follow(userId,userId);
        tweets[userId].insert({cnt++,tweetId});
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int> res;
        map<int,int> top10;
        for(auto it=friends[userId].begin();it!=friends[userId].end();it++){
            int t=*it;
            for(auto a=tweets[t].begin();a!=tweets[t].end();a++){
               top10.insert({a->first,a->second});
               if(top10.size()>10) top10.erase(top10.begin());
            }
        }
        for(auto it=top10.rbegin();it!=top10.rend();it++){
            res.push_back(it->second);
        }
        return res;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        friends[followerId].insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        if(followerId!=followeeId){
           friends[followerId].erase(followeeId); 
        }
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
```

# analysis
>由于获得新鲜事是需要按时间顺序排列的，那么我们可以用一个整型变量cnt来模拟时间点，每发一个消息，cnt自增1，那么我们就知道cnt大的是最近发的。
- 我们在建立用户和其所有消息之间的映射时，还需要建立每个消息和其时间点cnt之间的映射。
- 这道题的主要难点在于实现getNewsFeed()函数，这个函数获取自己和好友的最近10条消息，我们的做法是用户也添加到自己的好友列表中，然后遍历该用户的所有好友，遍历每个好友的所有消息，维护一个大小为10的哈希表，如果新遍历到的消息比哈希表中最早的消息要晚，那么将这个消息加入，然后删除掉最早的那个消息，这样我们就可以找出最近10条消息了.
- 这道题我也没有做出来，用cnt的方法当作时间，这个我没有想到，维护一个10的hash表，我也没有想法。欣赏一下，看来自己还需要磨练一下。

# reference
[[LeetCode] Design Twitter 设计推特][1]

[1]: http://www.cnblogs.com/grandyang/p/5577038.html