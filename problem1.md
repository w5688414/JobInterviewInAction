20
20
34  0   0   0   0   0   0   0   0   0   0   0   0   0   0   10  0   0   0   30
0   23  10  5   5   0   0   0   5   5   5   5   5   0   0   0   30  0   40  0
0   9   0   0   5   0   0   0   4   4   4   4   4   0   0   0   0   30  0   0
0   8   7   7   0   5   0   0   3   3   3   3   0   0   0   0   7   0   9   0
0   9   0   0   5   0   5   0   0   12  12  0   0   0   0   10  0   0   0   9
0   0   0   0   5   0   0   5   0   12  12  0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   12  12  0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   0   0   0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   0   0   0   0   5   0   0   0   0   0   0
40  30  3   6   6   0   0   0   0   0   0   0   0   5   5   0   0   0   10  0
0   0   20  0   0   6   6   0   0   0   0   0   0   0   5   6   5   10  10  0
40  30  3   7   6   0   0   0   0   0   0   0   0   0   0   6   0   0   10  0
0   0   0   0   0   0   0   17  0   0   0   0   17  0   0   6   5   7   7   0
0   0   0   0   0   0   0   0   7   0   0   7   0   0   0   0   0   0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   30  0   7   0   0   0   0   0   5   5   0   0   0   0   0   0   10  0   50
0   40  7   0   0   0   0   0   0   5   5   0   0   0   0   0   0   0   50  0
43  30  25  10  50  0   0   0   6   6   6   6   0   0   0   0   0   50  0   0



import java.util. * ;

public class Main {
	
	public static int DFS(int r, List<Integer>[] list, int[] dp) {
		if(dp[r] >= 0) {
			return dp[r];
		}
		dp[r] = 0;
		for (int i = 0; i < list[r].size(); i ++) {
			dp[r] += dfs(list[r].get(i), list, dp) + 1;
		}
		return dp[r];
	}

	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		sc.nextInt();
		List<Integer>[] list = new List[n];
		int[] dp = new int[n]; 
		for (int i = 0; i < n; i ++) {
			list[i] = new ArrayList<Integer>();
			dp[i] = -1;
		}
		for (int i = 0; i < m; i ++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			list[u].add(v);
		}
		int result = 0;
		for (int i = 0; i < n; i ++) {
			result = Math.max(result, DFS(i, list, dp));
		}
		System.out.println(result);
		sc.close();
	}
}

5
1, 1
1, 1
2, 0
0, 0
3, 0
singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
请播放周杰伦的七里香给我听

请播放 周杰伦/singer,actor 的 七里香/song 给我听