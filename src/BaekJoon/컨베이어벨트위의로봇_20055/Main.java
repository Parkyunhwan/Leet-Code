package BaekJoon.컨베이어벨트위의로봇_20055;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int [] belt;
    static int N, K;
    static long retValue = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        K = Integer.parseInt(s[1]);

        belt = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();

        boolean[] robot = new boolean[N];


        while(isOK()) {
            retValue++;
            // 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
            // 1.1 벨트 회전
            int temp = belt[belt.length - 1];
            for (int i = belt.length - 2; i >= 0; i--) {
                belt[i + 1] = belt[i];
            }
            belt[0] = temp;

            // 1.2 로봇도 함께 회전
            for (int i = robot.length - 1; i > 0; i--) {
                robot[i] = robot[i - 1];
            }
            robot[0] = false;

            // 2. 가장먼저올라간 로봇 부터 이동 (이동 칸에 내구도가 1이상 있을 때)
            robot[N - 1] = false;
            for (int i = robot.length - 1; i > 0; i--) {
                if (robot[i - 1] && belt[i] > 0 && !robot[i]) {
                    robot[i] = robot[i - 1];
                    robot[i - 1] = false;
                    belt[i]--;
                }
            }

            // 3. 올리는 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올림
            if (belt[0] > 0) {
                robot[0] = true;
                belt[0]--;
            }
        }
        System.out.println(retValue);
    }

    private static boolean isOK() {
        long count = Arrays.stream(belt).filter((b) -> b == 0).count();
        return count < K;
    }
}
