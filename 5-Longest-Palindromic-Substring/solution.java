public class Solution {
    public static String longestPalindrome(String s){
        String t = preprocess(s);
        int n = t.length();
        int[] result = new int[n];
        int right = 0, center = 0;
        for (int i = 1; i < n - 1; i++){
            int j = 2 * center - i;
            result[i] = (right > i) ? Math.min(right - i, result[j]): 0;
            while (t.charAt(i + 1 + result[i]) == t.charAt(i - 1 - result[i]))
                result[i]++;
            if (i + result[i] > right){
                center = i;
                right = i + result[i];
            }
        }

        int max = 0, maxIndex = 0;
        for (int i = 1; i < n - 1; i++){
            if (result[i] > max){
                max = result[i];
                maxIndex = i;
            }
        }
        int left = (maxIndex - 1 - max)/2;
        return s.substring(left, left + max);
    }

    public static String preprocess(String s){
        if (s.length() == 0 || s.isEmpty()){
            return "^$";
        }
        StringBuilder sb = new StringBuilder("^");
        for (int i = 0; i < s.length(); i++){
            sb.append("#").append(s.substring(i, i + 1));
        }
        sb.append("#$");
        return sb.toString();
    }
}