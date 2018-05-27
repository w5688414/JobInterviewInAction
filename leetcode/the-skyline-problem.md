# problem
>A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

# codes
```
class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int,int>> result;
        multiset<pair<int,int>> seq;
        for(auto p:buildings){
            seq.emplace(make_pair(p[0],-p[2]));
            seq.emplace(make_pair(p[1],p[2]));
        }
        multiset<int> height({0});
        pair<int,int> curr({0,0});
        for(auto p:seq){
            if(p.second<0){
                height.emplace(-p.second);
            }else{
                height.erase(height.find(p.second));
            }
            if(*height.rbegin()!=curr.second){
                curr.first=p.first;
                curr.second=*height.rbegin();
                result.push_back(curr);
            }
        }
        return result;
    }
};
```

# analysis
>这道题的解决方法还是很巧妙的，这个代码，我第一次看没看懂，原因对multiset的数据结构不熟，multiset的emplace函数会把数据按照键从小到大排列，我们就会得到
- (2,-10),(9,10),(3,-15),(7,15),(5,-12),(12,12),(15,-10),(20,10)
multiset 排序以后会得到
- (2,-10),(3,-15),(5,-12),(7,15),(9,10),(12,12),(15,-10),(20,10)
然后这个height每次也是从小到大排列的，自己模拟一下它的过程就知道它是怎么工作了的了。
# reference
[218. The Skyline Problem][1]
[The skyline problem][2]

[1]: https://leetcode.com/problems/the-skyline-problem/discuss/61197/(Guaranteed)-Really-Detailed-and-Good-(Perfect)-Explanation-of-The-Skyline-Problem?page=1
[2]: https://briangordon.github.io/2014/08/the-skyline-problem.html

