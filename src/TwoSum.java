//class Solution {
//    public int[] twoSum(int[] nums, int target) {
//        int i = 0;
//        int[] ret = new int[]{-1, -1};
//        while (i < nums.length) {
//            int j = i + 1;
//            while (j < nums.length) {
//                int sum = nums[i] + nums[j];
//                if (sum == target) {
//                    ret[0] = i;
//                    ret[1] = j;
//                    return ret;
//                }
//                j++;
//            }
//            i++;
//        }
//        return ret;
//    }
//}