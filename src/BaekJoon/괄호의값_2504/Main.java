package BaekJoon.괄호의값_2504;

import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<String> stack = new Stack<>();
        String[] split = sc.nextLine().split("");
        for (int i = 0; i < split.length; i++) {
            String curr = split[i];
            if (curr.equals("[") || curr.equals("(")) {
                stack.push(curr);
            } else if (curr.equals(")")) {
                int num = 0;
                while (!stack.isEmpty()) {
                    String pop = stack.pop();
                    if (pop.equals("(")) {
                        if (num == 0)
                            num = 1;
                        stack.push(String.valueOf(num * 2));
                        break;
                    } else if (pop.equals("[")) {
                        System.out.println("0");
                        return ;
                    } else {
                        num += Integer.parseInt(pop);
                    }
                }
            } else if (curr.equals("]")) {
                int num = 0;
                while (!stack.isEmpty()) {
                    String pop = stack.pop();
                    if (pop.equals("[")) {
                        if (num == 0)
                            num = 1;
                        stack.push(String.valueOf(num * 3));
                        break;
                    } else if (pop.equals("(")) {
                        System.out.println("0");
                        return ;
                    } else {
                        num += Integer.parseInt(pop);
                    }
                }
            }
            if (stack.isEmpty()) {
                System.out.println("0");
                return ;
            }
        }
        int sum;
        try {
            sum = stack.stream().mapToInt(Integer::parseInt).sum();
        } catch (NumberFormatException e) {
            System.out.println(0);
            return ;
        }
        System.out.println(sum);
    }
}
