# problem
>Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
# codes
```
/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point> &points) {
        if(points.size()<3)
            return points.size();

        int ret = 0;
        for(int i=0;i<points.size();i++){
            map<double,int> Map;
            int current_max=1;
            int ver_num=0;
            int hori_num=0;
            int repeat=0;
            for(int j=0;j<points.size();j++){
                if(i!=j){
                     double x=points[j].x-points[i].x;
                     double y=points[j].y-points[i].y;   
                    if(x==0&&y==0){
                        repeat++;
                    }
                    else if(x==0){
                        if(ver_num==0){
                            ver_num=2;
                        }else{
                            ver_num++;
                        }
                        current_max=max(current_max,ver_num); 
                    }else if(y==0){
                        if(hori_num==0){
                            hori_num=2; 
                        }else{
                            hori_num++;
                        }
                       current_max=max(current_max,hori_num); 
                    } else{
                        double k=y/x;
                        if(Map[k]==0){
                            Map[k]=2;
                        }else{
                            Map[k]++;
                        }
                        current_max=max(current_max,Map[k]); 
                    }
                }
            }
            ret=max(current_max+repeat,ret);
            
        }
        return ret;
    }
};

```

# analysis
>这道题目对我来说还是蛮难的，我只想到用斜率进行比较，但是斜率一样，不一定在同一条直线上；然后要考虑点相同的情况，以及点在坐标轴上。
# reference
[[编程题]max-points-on-a-line][1]
[1]: https://www.nowcoder.com/questionTerminal/bfc691e0100441cdb8ec153f32540be2