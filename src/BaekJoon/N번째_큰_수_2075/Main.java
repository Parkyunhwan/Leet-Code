package BaekJoon.N번째_큰_수_2075;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int curr = Integer.parseInt(st.nextToken());
                if (pq.size() == N) {
                    if (curr > pq.peek()) {
                        pq.poll();
                    } else {
                        continue;
                    }
                }
                pq.add(curr);
            }
        }
        System.out.println(pq.peek());
    }
}
