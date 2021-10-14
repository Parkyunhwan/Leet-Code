package BaekJoon.경사로_14890;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int [][] map;
    static int N, L;
    static int count = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(new BufferedInputStream(System.in)));
        String [] strs = br.readLine().split(" ");
        N = Integer.parseInt(strs[0]);
        L = Integer.parseInt(strs[1]);
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            map[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        for (int i = 0; i < N; i++) {
            int [] arr = Arrays.copyOf(map[i], N);

            if(extrDataTest(arr))
                count++;
            int [] arr2 = new int[N];
            for (int j = 0; j < N; j++) {
                arr2[j] = map[j][i];
            }

            if(extrDataTest(arr2)) {

                count++;
            }
        }
        System.out.println(count);
    }

    public static boolean extrDataTest(int [] row) {
        boolean [] flags = new boolean[N];
        for (int i = 0; i < N - 1; i++) {
            int diff = row[i + 1] - row[i];
            if (Math.abs(diff) > 1) // 높이가 1이상이면
                return false;
            if (diff == 1) { // 오르막길이면
                if (i - L + 1 < 0) // 앞에 경사로를 둘자리가 있는가?
                    return false;

                if (flags[i])
                    return false;
                for (int j = 1; j < L; j++) {
                    if (row[i] != row[i - j] || flags[i - j])
                        return false;
                    flags[i - j] = true;
                }
            }

            if (diff == -1) {
                if (i + L >= N)
                    return false;
                for (int j = 1; j < L + 1; j++) {
                    if (row[i] - 1 != row[i + j] || flags[i + j])
                        return false;
                    flags[i + j] = true;
                }
            }
        }
        return true;
    }
}
