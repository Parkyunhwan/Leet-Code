package BaekJoon.연산자끼워넣기;

import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int [] arr = new int[12];
    static int [] kiho = new int[5];
    static int [] save = new int[12];

    static int max_num = Integer.MIN_VALUE;
    static int min_num = Integer.MAX_VALUE;
    public static void main(String[] args) {

        // input
        Scanner sc = new Scanner(System.in);

        N = Integer.parseInt(sc.nextLine());
        String numbers = sc.nextLine();
        StringTokenizer st = new StringTokenizer(numbers);

        StringTokenizer st2 = new StringTokenizer(sc.nextLine());

        int i = 0;
        while (st.hasMoreTokens()) {
            arr[i] = Integer.parseInt(st.nextToken());
            i += 1;
        }

        i = 1;
        while (st2.hasMoreTokens()) {
            kiho[i] = Integer.parseInt(st2.nextToken());
            i += 1;
        }
        dfs( 0);
        System.out.println(max_num);
        System.out.println(min_num);
    }

    static void dfs(int index) {
        if (index == N - 1) {
            int sum = arr[0];
            for (int i = 0; i < N - 1; i++) {
                if (save[i] == 1) {
                    sum += arr[i + 1];
                } else if (save[i] == 2) {
                    sum -= arr[i + 1];
                } else if (save[i] == 3) {
                    sum *= arr[i + 1];
                } else {
                    sum /= arr[i + 1];
                }
            }
            max_num = Math.max(max_num, sum);
            min_num = Math.min(min_num, sum);
            return ;
        }
        for (int i = 1; i < 5; i++) {
            if (kiho[i] != 0) {
                kiho[i] -= 1;
                save[index] = i;
                dfs(index + 1);
                kiho[i] += 1;
                save[index] = 0;
            }
        }
    }
}
