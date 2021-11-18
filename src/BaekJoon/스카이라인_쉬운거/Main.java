package BaekJoon.스카이라인_쉬운거;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class Main {
    static Stack<Integer> st = new Stack<>();
    static int count = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i <= n; i++) {
            int x = 0;
            int y = 0;
            int [] pos;
            if (i < n) {
                pos = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                x = pos[0];
                y = pos[1];
            }
            if (i == n)
                y = 0;

            while (!st.isEmpty() && st.peek() > y) {
                st.pop();
                count++;
            }

            if (!st.isEmpty() && st.peek() == y)
                continue;

            st.push(y);
        }

        System.out.println(count);
    }
}
