package BaekJoon.쇠막대기_10799;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split("");
        Stack<String> stack = new Stack<>();
        String prev = "null";
        int count = 0;
        for (int i = 0; i < split.length; i++) {
            String val = split[i];
            if (val.equals("(")) {
                stack.add("(");
            } else if (val.equals(")")) {
                if (!stack.isEmpty()) {
                    stack.pop();

                    if (split[i - 1].equals("(")) {
                        count += stack.size();
                    } else {
                        count++;
                    }
                }
            }
        }

        System.out.println(count);
    }
}
