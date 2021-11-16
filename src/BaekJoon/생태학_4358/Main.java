package BaekJoon.생태학_4358;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> map = new HashMap<>();
        TreeMap<String, Double> tm = new TreeMap<>();
        StringBuilder sb = new StringBuilder();

        Double count = 0.0;
        String s = br.readLine();
        while(s != null && s.length() != 0) {
            map.put(s, map.getOrDefault(s, 0) + 1);
            count += 1.0;
            s = br.readLine();
        }

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            tm.put(entry.getKey(), (entry.getValue() / count) * 100.0);
        }

        Iterator<String> keyAll = tm.keySet().iterator();
        while(keyAll.hasNext()) {
            String ne = keyAll.next();
            sb.append(ne + " " + String.format("%.4f", tm.get(ne)) + "\n");
        }
        System.out.println(sb.toString());
    }
}
