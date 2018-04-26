# problem

牛牛准备在村庄内销售他秘制的青草。

 村庄内一共有n栋房子, n栋房子围成一个环, 即第n栋房子跟第1栋和第n-1栋房子相邻。

 经过调研,牛牛知道第i栋房子的住户需要购买xi份青草。

 因为牛牛的广告策略的原因, 如果他销售青草给某栋房子的住户, 那么他就不能销售青草给这栋房子相邻房子的住户。

 牛牛现在想知道他总共最多能卖出多少份青草。

 输入描述:
 输入的第一行为询问数t(1 <= t <= 100)。

 接下来每两行一个测试用例。

 第一行包含一个整数n(2 <= n <= 1000), 表示房子的数量。

 第二行n个正整数xi(1 <= xi <= 1000), 表示每栋房子住户需要购买的青草份数。

 输出描述:
 输出一个整数, 表示牛牛总共最多能卖出多少份青草。
 示例1
 输入
 ```
 2
 4
 8 9 2 8
 2
 10 100
 ```
 输出
 ```
 17
 100
 ```
# codes
## C++
```
import java.util. * ;

public class Main {

	static int[][] dp = new int[102][10002];
	static final int MOD = 100000007;
	
	public static void solution(int n, int k, int[] v) {
		for (int i = 0; i <= n; i ++) {
			for (int j = 0; j <= k; j ++) {
				dp[i][j] = 0;
			}
		}
		dp[0][0] = 1;
		for (int i = 1; i <= n; i ++) {
			for (int j = 0; j <= k; j ++) {
				dp[i][j] = dp[i - 1][j];
			}
			for (int j = v[i - 1]; j <= k; j ++) {
				dp[i][j] += dp[i][j - v[i - 1]];
				dp[i][j] %= MOD;
			}
		}
		System.out.println(dp[n][k]);
	}

	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while (t-- > 0) {
			int n = sc.nextInt();
			int k = sc.nextInt();
			int[]v = new int[n];
			sc.nextLine();
			for (int i = 0; i < n; i++)
				v[i] = sc.nextInt();
			sc.nextLine();
			solution(n, k, v);
		}
		sc.close();
	}
}

```

## C++
```
//
//  zhaoyin_demo2.cpp
//  Demo
//
//  Created by eric on 4/22/18.
//  Copyright © 2018 eric. All rights reserved.
//

#include "zhaoyin_demo2.hpp"
#include<iostream>
#include<vector>
using namespace std;

int dp[1002][2][2];
int solution(int n,vector<int> a){
    for(int i=0;i<n;i++){
        for(int j=0;j<2;j++){
            for(int k=0;k<2;k++){
                dp[i][j][k]=0;
            }
        }
    }
    dp[0][1][1]=a[0];
    dp[1][0][1]=a[1];
    dp[1][1][0]=a[0];
    for(int i=2;i<n-1;i++){
        for(int j=0;j<2;j++){
            dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j][1]);
            dp[i][j][1]=dp[i - 1][j][0] + a[i];
        }
    }
    if(n>2){
        dp[n-1][0][0]=max(dp[n-2][0][1],dp[n-2][0][0]);
        dp[n-1][0][1]=dp[n-2][0][0]+a[n-1];
        dp[n-1][1][0]=max(dp[n-2][1][0],dp[n-2][1][1]);
    }
    return max(max(dp[n-1][0][0],dp[n-1][0][1]),dp[n-1][1][0]);
}

int main(){
    int t;
    cin>>t;
    int max_val=-1;
    for(int i=0;i<t;i++){
        int n;
        cin>>n;
        vector<int> vec;
        int num=0;
        for(int j=0;j<n;j++){
            cin>>num;
            vec.push_back(num);
        }
        max_val=solution(n, vec);
        cout<<max_val<<endl;
    }
    return 0;
}

```

