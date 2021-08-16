//class Solution {
//    public int reverse(int x) {
//        long stack = 0;
//        long remainder;
//
//        while (x != 0) {
//            remainder = x % 10; // 음수의 나머지는 음수로 나온다....!! 그래서 음수 검사가 따로 필요 없었다.
//            x /= 10;
//            stack *= 10;
//            stack += remainder;
//        }
//
//        if (Integer.MIN_VALUE <= stack && stack <=  Integer.MAX_VALUE)
//            return (int)stack;
//        else
//            return 0;
//    }
//}