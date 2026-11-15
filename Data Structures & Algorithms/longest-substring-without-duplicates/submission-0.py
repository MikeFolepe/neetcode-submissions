class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        for i in range(len(s)):
            substring = set()
            substring.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in substring:
                    break
                substring.add(s[j])
                
            maxLength = max(maxLength, len(substring))

        return maxLength
            