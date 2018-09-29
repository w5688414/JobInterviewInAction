## p1
```
某网站的数据库有一个成绩表myscore，希望找出成绩表中平均得分小于90的所有试卷。

select paper_id from myscore group by paper_id having avg(score) < 90
```
## p2
```
某棵完全二叉树上有698个节点，则该二叉树的叶子节点数为
349

如果一棵具有n个结点的深度为k的二叉树，它的每一个结点都与深度为k的满二叉树中编号为1~n的结点一一对应，这棵二叉树称为完全二叉树。
可以根据公式进行推导，假设n0是度为0的结点总数（即叶子结点数），n1是度为1的结点总数，n2是度为2的结点总数，由二叉树的性质可知：n0＝n2＋1，则n= n0＋n1＋n2（其中n为完全二叉树的结点总数），由上述公式把n2消去得：n= 2n0+n1－1，由于完全二叉树中度为1的结点数只有两种可能0或1，由此得到n0＝（n＋1）/2或n0＝n/2，合并成一个公式：n0＝取整（（n＋1）/2），就可根据完全二叉树的结点总数计算出叶子结点数。

```

## p3
```
一个有序数列，序列中的每一个值都能够被2或者3或者5所整除，这个序列的初始值从1开始，但是1并不在这个数列中。求第1500个值是多少？
```
```
2、3、5的最小公倍数是30。[ 1, 30]内符合条件的数有22个。如果能看出[ 31, 60]内也有22个符合条件的数，那问题就容易解决了。也就是说，这些数具有周期性，且周期为30.
       第1500个数是：1500/22=68   1500%68=4。也就是说：第1500个数相当于经过了68个周期，然后再取下一个周期内的第4个数。一个周期内的前4个数：2,3,4,5。
故，结果为68*30=2040+5=2045


在区间 [1, 30] 中，
能被2整除的数有 30 / 2 = 15 个，
能被3整除的数有 30 / 3 = 10 个，
能被5整除的数有 30 / 5 = 6 个，
能被2整除也能被3整除的数有 30 / 6 = 5 个，
能被2整除也能被5整除的数有 30 / 10 = 3 个，
能被3整除也能被5整除的数有 30 / 15 = 2 个，
能被2整除、能被3整除也能被5整除的数有 30 / 30 = 1 个，
根据集合的容斥定律可知：A∪B∪C = A + B + C - A ∩ B - B ∩ C - A ∩ C + A ∩ B ∩ C，
因此，能被2整除或能被3整除或能被5整除的数的个数（不重复）为： 15 + 10 + 6 - 5 - 3 - 2 + 1 = 22
1500 / 22 = 68 ··· 4，[ 1, 30] 中，第4个满足条件的数是 5 ，而 68 * 30 = 2040， 因此第1500个数为
2040 + 5 = 2045 (2,3,4,5)
```
## p4
```
class program
 {
     static void Main(string[] args)
     {
         int i;
         i = x(x(8));
     }
     static int x(int n)
     {
         if (n <= 3)
             return 1;
         else
             return x(n - 2) + x(n - 4) + 1;
     }
 }
```
递归算法x(x(8))需要调用几次函数x(int n)?

```
根据题意，易得x(3) = x(2) = x(1) = x(0) = 1
x(8) = x(6) +x(4) +1
       = x(4) + x(2) +1 + x(2) + x(0) +1 + 1 
        = x(2) + x(0) +1 + 1 + 1 +1 + 1 +1 + 1 
       = 9 
x(8)  这个就调用了9次函数x(int n)
同理可得x(9)也是调用了9次函数x(int n)
所以总共18次。
```
## p5
```
若以{4,5,6,7,8}作为叶子结点的权值构造哈夫曼树，则其带权路径长度是（）。
```
```
树的带权路径长度(Weighted Path Length of Tree)：定义为树中所有叶结点的带权路径长度之和。
结点的带权路径长度：结点到树根之间的路径长度与该结点上权的乘积。
构造哈夫曼树后，
4,5的编码长度为3,
6,7,8的编码长度为2
（4+5）*3+（6+7+8）*2=27+42=69
```

- 参考 https://www.nowcoder.com/questionTerminal/ab6e3f5726fd41009c136ea4c6c26d86