class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t) or not s or not t:
            return ""
       
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        required = len(t_count)  
        formed = 0
        
        window_counts = {}  
        left = 0
        min_window = ""
        min_len = float("inf")
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                char = s[left]
                window_counts[char] -= 1
            
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                left += 1
        
        return min_window