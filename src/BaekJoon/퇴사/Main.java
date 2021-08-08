package BaekJoon.퇴사;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int [][] arr = new int [N][2];
        int [] dp = new int[N];

        for (int i = 0; i < arr.length; i++) {
            String [] s = br.readLine().split(" ");
            arr[i][0] = Integer.parseInt(s[0]);
            arr[i][1] = Integer.parseInt(s[1]);
            dp[i] = arr[i][1];
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (i - j >= arr[j][0]) {
                    dp[i] = Math.max(dp[i], dp[j] + arr[i][1]);
                }
            }
        }

        int max = 0;
        for (int i = 0; i < N; i++) {
            if (i + arr[i][0] <= N) {
                if (max < dp[i])
                    max = dp[i];
            }
        }
        System.out.println(max);
    }
}
