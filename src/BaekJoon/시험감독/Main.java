package BaekJoon.시험감독;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int examNum = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[examNum];
        for (int i = 0; i < examNum; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int ju = Integer.parseInt(st.nextToken());
        int bu = Integer.parseInt(st.nextToken());

        long count = 0;
        for (int i = 0; i < examNum; i++) {
            arr[i] -= ju;
            count += 1;
            if (arr[i] <= 0)
                continue;
            if (arr[i] > 0) {
                count += (arr[i] / bu);
                if (arr[i] % bu != 0) {
                    count += 1;
                }
            }
        }

        System.out.println(count);
    }
}
