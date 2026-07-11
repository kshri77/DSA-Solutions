class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left=0;
        int maxlen=0;
        Map<Character, Integer> seen = new HashMap<>();
        for (int right=0;right<s.length();right++){
            char currentChar = s.charAt(right);
            if (seen.containsKey(currentChar) && seen.get(currentChar)>=left){
                left=seen.get(currentChar)+1;

            }
            seen.put(currentChar, right);
            maxlen = Math.max(maxlen, right - left + 1);
        }
        return maxlen;
    }
}