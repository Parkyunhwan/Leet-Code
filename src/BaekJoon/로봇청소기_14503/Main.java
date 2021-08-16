package BaekJoon.로봇청소기_14503;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    private static int N, M, r, c, d;
    private static BufferedReader br;
    private static StringTokenizer st;
    private static int [][] arr;
    private static final int [] dx = {-1, 0, 1, 0};
    private static final int [] dy = {0, 1, 0, -1};
    static int count = 0;

    public static void main(String[] args) throws IOException {
        input();
        solve();
        System.out.println(count);
    }

    public static void input() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        arr = new int[N + 1][M + 1];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int j = 0;
            while (st.hasMoreTokens()) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                j++;
            }
        }
    }

    public static void solve() {
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(r, c, d));
        boolean check = false;
        boolean stop = false;

        while (!q.isEmpty()) {
            Pair p = q.poll();
            check = false;

            /*
                1. 문제풀이에 오류가 생긴 부분
                큐 형식으로 풀었을 때 후진 시에도 동일하게 아래 if문을 지나게 된다.
                따라서 청소가 가능할 경우에만 count를 증가 시켜 주자.
             */
            if (arr[p.x][p.y] == 0) {
                arr[p.x][p.y] = 2;
                count++;
            }

            for (int i = 1; i < 5; i++) {
                int dir = p.direction - i < 0 ? p.direction - i + 4: p.direction - i;
                int nx = p.x + dx[dir];
                int ny = p.y + dy[dir];
                if (nx < 0 || nx >= N || ny < 0 || ny >= M || arr[nx][ny] != 0) {
                    continue;
                }
                if (arr[nx][ny] == 0) {
                    q.add(new Pair(nx, ny, dir));
                    check = true;
                    break;
                }
            }

            // 한칸 후진을 하고 큐에 넣기
            if (!check) {
                int nx;
                int ny;
                nx = p.x - dx[p.direction];
                ny = p.y - dy[p.direction];
                if (nx < 0 || nx >= N || ny < 0 || ny >= M || arr[nx][ny] == 1)
                    stop = true;
                else
                    q.add(new Pair(nx, ny, p.direction));
            }

            if (stop)
                break;
        }
    }

    private static class Pair {
        int x;
        int y;
        int direction;
        public Pair(int x, int y, int direction) {
            this.x = x;
            this.y = y;
            this.direction = direction;
        }
    }
}
