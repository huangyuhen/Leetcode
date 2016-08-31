public class Solution {
    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        for (int start = s.length() - 1; start >=0; start--){
        	if (s.charAt(start) == ' ') continue;
        	int end = start;
        	while (start >= 0 && s.charAt(start) != ' ') start--;
        	sb.append(s.substring(start+1,end+1)).append(" ");
        }
        return sb.toString().trim();
    }
}