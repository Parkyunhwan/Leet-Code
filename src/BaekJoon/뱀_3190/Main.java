/*
* https://www.acmicpc.net/source/20104017
* 위 링크처럼 뱀의 size를 저장해두고 맵에 기록된 시간과 비교해서 중복을 판단하는 것도 하나의 방법이다.
* 이렇게 푸는 형식이 꽤 있는 것 같다.
* */
package BaekJoon.뱀_3190;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static final int APPLE = -1;
    static final int SNAKE = 1;

    static int N, K, L;
    static int[][] map = new int[101][101];
    static int time = 1;

    static int [] dx = {0, 1, 0, -1};
    static int [] dy = {-1, 0, 1, 0};
    static int currDir = 2;
    static List<DirClass> dirList = new ArrayList<>();
    static Deque<Pair> snake = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());

        //사과는 -1로 표현
        for (int i = 0; i < K; i++) {
            int[] pos = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            map[pos[0]][pos[1]] = APPLE;
        }

        L = Integer.parseInt(br.readLine());
        for (int i = 0; i < L; i++) {
            String [] str = br.readLine().split(" ");
            int num = Integer.parseInt(str[0]);
            String nextDir = str[1];
            dirList.add(new DirClass(num, nextDir));
        }
        solve();
        System.out.println(time);
    }

    private static void solve() {
        int x = 1;
        int y = 1;

        map[x][y] = SNAKE;
        snake.addLast(new Pair(x, y));
        while(true) {
            if (!dirList.isEmpty()) {
                DirClass dirClass = dirList.get(0);
                if (dirClass.num == time - 1) {
                    changeDir(dirClass.nextDir);
                    dirList.remove(0);
                }
            }
            int nx = x + dx[currDir];
            int ny = y + dy[currDir];

            if (isConfict(nx, ny))
                break;
            if (map[nx][ny] != APPLE) {
                if (!snake.isEmpty()) {
                    Pair pair = snake.removeFirst();
                    map[pair.x][pair.y] = 0;
                }
            }
            snake.addLast(new Pair(nx, ny));
            map[nx][ny] = SNAKE;
            x = nx;
            y = ny;
            time++;
        }
    }

    private static void changeDir(String nextDir) {
        if (nextDir.equals("L")) {
            currDir = (currDir + 1) % 4;
        } else {
            if (currDir == 0)
                currDir = 3;
            else
                currDir = (currDir - 1) % 4;
        }
    }

    private static boolean isConfict(int x, int y) {
        if (x < 1 || y < 1 || x > N || y > N)
            return true;
        if (map[x][y] == SNAKE)
            return true;
        return false;
    }

    static class Pair{
        int x;
        int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static class DirClass{
        public int num;
        public String nextDir;

        public DirClass(int num, String nextDir) {
            this.num = num;
            this.nextDir = nextDir;
        }
    }
}
