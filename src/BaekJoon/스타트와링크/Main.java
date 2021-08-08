package BaekJoon.스타트와링크;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static BufferedReader br;
    static int [][] arr;
    static int N;
    static boolean [] visited;
    static int result = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        input();
        solve(0, 0);

        System.out.println(result);
    }

    private static void input() throws IOException{
        br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        visited = new boolean[N];
        for (int i = 0; i < N; i++) {
            String[] strs = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(strs[j]);
            }
        }
    }

    private static void solve(int start, int num) {
        if (num == N / 2) {
            int team1 = 0;
            int team2 = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (visited[i] && visited[j]) {
                        team1 += arr[i][j];
                    } else if (visited[i] == false && !visited[j]) {
                        team2 += arr[i][j];
                    }
                }
            }
            result = Math.min(result, Math.abs(team1 - team2));
            return;
        }

        for (int i = start; i < N; i++) {
            visited[i] = true;
            solve(i + 1, num + 1);
            visited[i] = false;
        }
    }
}
