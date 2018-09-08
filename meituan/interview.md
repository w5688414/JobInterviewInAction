美团一面
1.item based collaborative filtering， user based collaborative filterating的区别。讲一下AUC，roc
2.你了解hadoop，spark框架吗？跟我讲讲hadoop数据处理要怎么做？
3.讲一下矩阵分解，讲一下SVD方法
4.讲一下tensorflow的分布式
5.一个数组，数组里面的值是整形，然后求组合出来的最小值。
6.深度学习的梯度消失，梯度爆炸是怎么回事？讲一下batchnormalization是怎么回事？
7.怎样防止过拟合？
8.java的接口和抽象类有啥区别？

# user based CF and item based CF
当系统中用户量很大，而物品数量相对固定的时候，适合用item-based方法，例如电影、视频推荐等；当系统中物品数量很大，而用户数量相对固定的时候，适合用user-based方法，例如新闻推荐等。

推荐系统user-based和item-based协同过滤算法定性比较. https://blog.csdn.net/u012845311/article/details/64919021

在现实的情况中，往往物品的个数是远远小于用户的数量的，而且物品的个数和相似度相对比较稳定，可以离线完成工作量最大的相似性计算步骤，从而大大降低了在线计算量，基于用户的实时性更好一些。但是具体使用的场景，还需要根据具体的业务类型来区分，User-CF偏重于反应用户小群体热点，更具社会化，而Item-CF在于维持用户的历史兴趣，比如：对于新闻、阅读类的推荐，新闻阅读类的信息是实时更新的，所以ItemCF在这种情况下需要不断更新，而用户对新闻的个性化推荐不是特别的强烈情况，用户有新行为不会导致相似用户的剧烈运动。