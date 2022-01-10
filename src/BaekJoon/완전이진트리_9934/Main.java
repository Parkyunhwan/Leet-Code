package BaekJoon.완전이진트리_9934;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n;
    static String [] s;
    static StringBuilder [] floor;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        s = br.readLine().split(" ");

        floor = new StringBuilder[n];
        for (int i = 0; i < n; i++) {
            floor[i] = new StringBuilder();
        }

        makeInOrderToTree(0, s.length, 0);

        for (int i = 0; i < n; i++) {
            System.out.println(floor[i].toString());
        }
    }

    static void makeInOrderToTree(int start, int end, int level) {
        if (level >= n)
            return ;
        int mid = (int)((start + end)/2);
        floor[level].append(s[mid] + " ");

        makeInOrderToTree(start, mid - 1, level + 1);
        makeInOrderToTree(mid + 1, end, level + 1);
    }
}
