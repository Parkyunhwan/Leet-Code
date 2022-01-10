package BaekJoon.스택_수열_1874;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        int curr = 1;

        int n = sc.nextInt();
        int start = 0;
        for (int i = 0; i < n; i++) {
            int value = sc.nextInt();

            if (value > start) {
                for (int j = start + 1; j <= value; j++) {
                    stack.push(j);
                    sb.append("+\n");
                }
                start = value;
            }
            else if (stack.peek() != value) {
                System.out.println("NO");
                return;
            }

            stack.pop();
            sb.append("-\n");
        }

        System.out.println(sb.toString());
    }
}
