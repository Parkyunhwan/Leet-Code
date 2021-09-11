package BaekJoon.상어초등학교_21608;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int [][] map;
    static Map<Integer, List<Integer>> studentLike = new HashMap<>();
    static int n;
    static List<Node> curr;
    static int score = 0;
    static BufferedReader br;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        init();
        addStudentToClassroom();
        System.out.println(calculateScore());
    }

    private static void addStudentToClassroom() throws IOException {
        for (int i = 0; i < n * n; i++) {
            String[] s = br.readLine().split(" ");
            int num = Integer.parseInt(s[0]);
            List<Integer> tmp = new ArrayList<>();
            curr = new ArrayList<>();

            for (int j = 1; j < 5; j++) {
                tmp.add(Integer.parseInt(s[j]));
            }
            studentLike.put(num, tmp);

            selectStudentPosition(num);
            Collections.sort(curr);

            Node node = curr.get(0);
            map[node.x][node.y] = num;
        }
    }

    private static void init() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new int[n + 1][n + 1];

        for (int i = 0; i < n; i++) {
            Arrays.fill(map[i], -1);
        }
    }

    private static int calculateScore() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int count = 0;
                int currNum = map[i][j];

                for (int k = 0; k < 4; k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];

                    if (nx < 0 || ny < 0 || nx >= n || ny >= n)
                        continue;
                    if (studentLike.get(currNum).contains(map[nx][ny])) {
                        count++;
                    }
                }

                if (count == 4)
                    score += 1000;
                else if (count == 3)
                    score += 100;
                else if (count == 2)
                    score += 10;
                else if (count == 1)
                    score += 1;
            }
        }
        return score;
    }

    public static void selectStudentPosition(int num) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == -1) {
                    Node node = new Node();
                    // empty
                    int emptyNum = 0;
                    int likeNum = 0;
                    for (int k = 0; k < 4; k++) {
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        if (nx < 0 || ny < 0 || nx >= n || ny >= n)
                            continue;
                        if (map[nx][ny] == -1) {
                            emptyNum++;
                        }

                        if (studentLike.get(num).contains(map[nx][ny])) {
                            likeNum++;
                        }
                    }
                    node.x = i;
                    node.y = j;
                    node.empty = emptyNum;
                    node.like = likeNum;
                    curr.add(node);
                }
            }
        }
    }

    static class Node implements Comparable<Node>{
        int x;
        int y;
        int empty;
        int like;

        @Override
        public int compareTo(Node o) {
            if (o.like != this.like) {
                return o.like - this.like;
            }

            if (o.empty != this.empty) {
                return o.empty - this.empty;
            }

            if (o.x != this.x) {
                return this.x - o.x;
            }

            return this.y - o.y;
        }
    }
}