package BaekJoon.데이터체커_22942;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Pair> pq = new PriorityQueue<>(new Comparator<Pair>() {
            @Override
            public int compare(Pair o1, Pair o2) {
                return o1.value - o2.value;
            }
        });
        Stack<Pair> st = new Stack<>();
        StringBuilder sb = new StringBuilder();
        int i = Integer.parseInt(br.readLine());
        while (i-- != 0) {
            String[] split = br.readLine().split(" ");
            int x = Integer.parseInt(split[0]);
            int r = Integer.parseInt(split[1]);
            int left = x - r;
            int right = x + r;
            pq.add(new Pair(left, i, "["));
            pq.add(new Pair(right, i, "]"));
        }

        while(!pq.isEmpty()) {
            Pair poll = pq.poll();
            String dir = poll.dir;
            int num = poll.num;
            if (dir.equals("[")) {
                st.add(poll);
            } else if (dir.equals("]")) {
                if (st.isEmpty()) {
                    sb.append("NO");
                    break;
                } else {
                    Pair pop = st.pop();
                    if (!pop.dir.equals("[") || pop.num != num) {
                        sb.append("NO");
                        break;
                    }
                }
            }
        }

        if (sb.length() == 0) {
            if (st.isEmpty()) {
                sb.append("YES");
            } else {
                sb.append("NO");
            }
        }

        System.out.println(sb);
    }

    static class Pair{
        int value;
        String dir;
        int num;

        Pair(int value, int num, String dir) {
            this.value = value;
            this.num = num;
            this.dir = dir;
        }
    }
}
