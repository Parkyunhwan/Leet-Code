package BaekJoon.소수_찾기_1978;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int count = 0;

        int[] values = Arrays.stream(sc.nextLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();




        for (int i = 0; i < values.length; i++) {

            int value = values[i];
            if (myPrime(value))
                count++;
        }

        System.out.println(count);
    }

    private static boolean myPrime(int value) {
        if (value < 2) {
            return false;
        }
        boolean flag = false;
        for (int div = 2; div < value; div++) {
            if (value % div == 0) {
                return false;
            }
        }
        return true;
    }
}
