package BaekJoon.AC_5430;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        Deque<String> dq = new ArrayDeque<>();

        for (int i = 0; i < t; i++) {
            String p = sc.next();
            int n = sc.nextInt();

            String arr = sc.next();
            String[] split = arr.substring(1, arr.length() - 1).split(",");

            for(int j = 0; j < n; j++)
                dq.add(split[j]);

            ac(dq, p);
        }
    }

    static void ac(Deque<String> dq, String p) {
        boolean reverse = false;

        for (int i = 0; i < p.length(); i++) {
            char command = p.charAt(i);

            if (command == 'R') {
                reverse = !reverse;
            } else if (command == 'D') {
                if (dq.isEmpty()) {
                    System.out.println("error");
                    return;
                }

                if (!reverse)
                    dq.removeFirst();
                else
                    dq.removeLast();
            }
        }

        StringBuilder sb = new StringBuilder("[");
        while (!dq.isEmpty()) {
            if (reverse)
                sb.append(dq.removeLast());
            else
                sb.append(dq.removeFirst());
            if(!dq.isEmpty())
                sb.append(',');
        }
        sb.append("]");
        System.out.println(sb);

    }
}
