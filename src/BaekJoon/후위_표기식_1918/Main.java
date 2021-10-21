package BaekJoon.후위_표기식_1918;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static Stack<String> st = new Stack<>();
    static String [] strs;
    static Map<String, Integer> prio = new HashMap<>();
    static String opers = "*/+-()";
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(new BufferedInputStream(System.in)));
        StringBuilder stringBuilder = new StringBuilder();

        prio.put("*", 3);
        prio.put("/", 3);
        prio.put("+", 2);
        prio.put("-", 2);
        prio.put("(", 1);
        prio.put(")", 1);

        strs = br.readLine().split("");

        for (int i = 0; i < strs.length; i++) {
            String str = strs[i];
            if (!opers.contains(str)) { // 알파벳은 바로 출력
                stringBuilder.append(str);
            }
            else { // 연산자라면
                if (st.isEmpty() || "(".equals(str)) {
                    st.add(str);
                } else {
                    // 우선순위 계산할 것
                    int currPrio = prio.get(str);
                    while (!st.isEmpty() && currPrio <= prio.get(st.peek())) {// 우선순위가 스택보다 같거나 낮다면 현재값의 우선순위가 가장 높아질 때 까지 스택에 있는 값 빼서 출력 후 현재값 스택에 삽입
                        if (")".equals(str) && "(".equals(st.peek())) {
                            st.pop();
                            break;
                        }
                        stringBuilder.append(st.pop());
                    }
                    if (")".equals(str))
                        continue;

                    if (st.isEmpty() || currPrio > prio.get(st.peek())) { // 우선순위가 스택보다 높다면..삽입
                        st.add(str);
                    }
                }
            }
        }

        while (!st.isEmpty()) {
            stringBuilder.append(st.pop());
        }
        String s = stringBuilder.toString();
        System.out.println(s);
    }

}
