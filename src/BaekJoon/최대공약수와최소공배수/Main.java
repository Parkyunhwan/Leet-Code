package BaekJoon.최대공약수와최소공배수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] in = br.readLine().split(" ");
        System.out.println(gcd(Integer.parseInt(in[0]), Integer.parseInt(in[1])));
        System.out.println(lcm(Integer.parseInt(in[0]), Integer.parseInt(in[1]), gcd(Integer.parseInt(in[0]), Integer.parseInt(in[1]))));

        br.close();
    }

    private static int lcm(int parseInt, int parseInt1, int gcd) {
        return parseInt * parseInt1 / gcd;
    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}
