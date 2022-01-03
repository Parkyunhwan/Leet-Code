package BaekJoon.문제추천시스템_version1_21939;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Pair> pq_min = new PriorityQueue<>(new Comparator<Pair>() {
            @Override
            public int compare(Pair o1, Pair o2) {
                if (o1.l == o2.l) {
                    return o1.p - o2.p;
                } else {
                    return o1.l - o2.l;
                }
            }
        });
        PriorityQueue<Pair> pq_max = new PriorityQueue<>(new Comparator<Pair>() {
            @Override
            public int compare(Pair o1, Pair o2) {
                if (o1.l == o2.l) {
                    return o2.p - o1.p;
                } else {
                    return o2.l - o1.l;
                }
            }
        });
        Map<Integer, Integer> map = new HashMap<>();
        int N = stoi(br.readLine());
        for(int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            int p = stoi(s[0]);
            int l = stoi(s[1]);
            Pair pair = new Pair(p, l);
            pq_min.add(pair);
            pq_max.add(pair);
            map.put(p, l);
        }

        int M = stoi(br.readLine());
        for (int i = 0; i < M; i++) {
            String[] s = br.readLine().split(" ");
            if (s[0].equals("add")) {
                int p = stoi(s[1]);
                int l = stoi(s[2]);
                pq_min.add(new Pair(p, l));
                pq_max.add(new Pair(p, l));
                map.put(p, l);
            } else if (s[0].equals("recommend")) {
                if (s[1].equals("1")) {
                    while (true) {
                        Pair poll = pq_max.peek();
                        if (map.getOrDefault(poll.p, 0) != poll.l) {
                            pq_max.remove();
                            continue;
                        }
                        else {
                            //map.remove(poll.p);
                            sb.append(poll.p + "\n");
                            break;
                        }
                    }
                } else if (s[1].equals("-1")) {
                    while (true) {
                        Pair poll = pq_min.peek();
                        if (map.getOrDefault(poll.p, 0) != poll.l) {
                            pq_min.remove();
                            continue;
                        }
                        else {
                            //map.remove(poll.p);
                            sb.append(poll.p + "\n");
                            break;
                        }
                    }
                }
            } else if (s[0].equals("solved")) {
                map.remove(stoi(s[1]));
            }
        }
        System.out.println(sb.toString());
    }

    static int stoi(String str) {
        return Integer.parseInt(str);
    }

    static class Pair{
        int p;
        int l;

        public Pair(int p, int l) {
            this.p = p;
            this.l = l;
        }
    }
}
