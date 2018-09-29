
## 多部完全图
```

#include<bits/stdc++.h>
using namespace std;
const int MAXN = 1e3 + 10;
std::vector<int> v[MAXN];
int mp[MAXN][MAXN];
string vis[MAXN];
int main() {
    int t;
    cin >> t;
    while(t--) {
        memset(mp, 0, sizeof(mp));
        for(int i = 1; i < MAXN; ++i) vis[i] = "";
        int n, m;
        cin >> n >> m;
        for(int i = 0; i < m; ++i) {
            int x, y;
            cin >> x >> y;
            v[x].push_back(y);
            v[y].push_back(x);
            mp[x][y] = 1;
            mp[y][x] = 1;
        }
        string sol = "Yes";
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= n; ++j) {
                if(mp[i][j]) {
                    vis[i] += j + '0';
                }
            }
        }
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= n; ++j) {
                if(i == j) continue;
                if(mp[i][j] != 1) {
                    if(vis[i] != vis[j]) {
                        sol = "No";
                    }
                }
            }
        }
        cout << sol << endl;
    }
    return 0;
}
```
京东c++ 两题ac题解. https://www.nowcoder.com/discuss/106148?type=2&order=0&pos=4&page=1