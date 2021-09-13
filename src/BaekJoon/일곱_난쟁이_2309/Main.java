
// 재귀 시 바로 종료를 위해서는 System.exit(0)를 이용한다. 단순 return을 통해 바로 복귀 못함.
package BaekJoon.일곱_난쟁이_2309;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static List<Integer> list = new ArrayList<>();
    static int[] smallMan = new int[9];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        for (int i = 0; i < 9; i++) {
            smallMan[i] = Integer.parseInt(br.readLine());
        }

        findRealMans(0, 0);
    }

    private static void findRealMans(int index, int curr) {
        if (index == 7) {
            int sum = list.stream().mapToInt(i -> i).sum();

            if (sum == 100) {
                list.stream().sorted().forEach(System.out::println);
                System.exit(0);
            }
        }
        for (int i = curr; i < 9; i++) {
            list.add(smallMan[i]);
            findRealMans(index + 1, i + 1);
            list.remove(list.size() - 1);
        }
    }
}
