package BaekJoon.문자열문제.그룹단어체커_1316;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;


        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            char prev = str.charAt(0);
            Set<Character> set = new HashSet<>();
            //Map<Character, Boolean> map = new HashMap<>();
            set.add(prev);
            //map.put(prev, true);
            boolean flag = true;
            for (int j = 1; j < str.length(); j++) {
                if (prev != str.charAt(j)) {
                    if (set.contains(str.charAt(j))) {
                        flag = false;
                        break;
                    }
                    else
                        set.add(str.charAt(j));
                }
                prev = str.charAt(j);
            }
            if (flag)
                count++;
        }
        System.out.println(count);
    }
}
