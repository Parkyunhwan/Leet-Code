//
package BaekJoon.문자열문제.경고_3029;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String currTime = br.readLine();
        String throwTime = br.readLine();

        String[] currTimes = currTime.split(":");
        String[] throwTimes = throwTime.split(":");

        long currSeconds = Long.parseLong(currTimes[0]) * 60 * 60
                + Long.parseLong(currTimes[1]) * 60
                + Long.parseLong(currTimes[2]);

        long throwSeconds = Long.parseLong(throwTimes[0]) * 60 * 60
                + Long.parseLong(throwTimes[1]) * 60
                + Long.parseLong(throwTimes[2]);

        if (throwSeconds < currSeconds)
            throwSeconds += (60 * 60 * 24);

        long waitSeconds = throwSeconds - currSeconds;

        long waitHour, waitMinute, waitSecond;

        if (waitSeconds == 0) {
            waitHour = 24;
            waitMinute = 0;
            waitSecond = 0;
        } else {
            waitSecond = waitSeconds % 60;
            waitSeconds /= 60;
            waitMinute = waitSeconds % 60;
            waitHour = waitSeconds / 60;
        }
        System.out.println(String.format("%02d",waitHour) + ":" + String.format("%02d",waitMinute) + ":" + String.format("%02d",waitSecond));
    }
}
