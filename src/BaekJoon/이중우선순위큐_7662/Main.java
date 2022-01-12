package BaekJoon.이중우선순위큐_7662;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int k = Integer.parseInt(br.readLine());
            operation(k);
        }
    }

    static void operation(int k) throws IOException {
        PriorityQueue<Integer> pq_min = new PriorityQueue<>();
        PriorityQueue<Integer> pq_max = new PriorityQueue<>(Comparator.reverseOrder());
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < k; i++) {
            String [] strs = br.readLine().split(" ");
            String oper = strs[0];
            int value = Integer.parseInt(strs[1]);

            if ("I".equals(oper)) {
                pq_min.add(value);
                pq_max.add(value);
                map.put(value, map.getOrDefault(value, 0) + 1);
            } else if ("D".equals(oper)) {
                // 비어있다면 무시
                if (map.size() == 0)
                    continue;

                if (value == 1) {
                    validate(pq_max, map);
                } else if (value == -1) {
                    validate(pq_min, map);
                }
            }
        }
        if (map.size() == 0) {
            System.out.println("EMPTY");
        } else {
            int max = validate(pq_max, map);
            int min = map.size() > 0 ? validate(pq_min, map) : max;
            System.out.println(max + " " + min);
        }
    }

    static int validate(PriorityQueue<Integer> pq, Map<Integer, Integer> map) {
        int num;
        while (true) {
            num = pq.poll();
            int cnt = map.getOrDefault(num, 0);

            if (cnt > 1) {
                map.put(num, map.get(num) - 1);
                break;
            } else if (cnt == 1) {
                map.remove(num);
                break;
            }
        }
        return num;
    }
}
