class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        count, maxf = {}, 0
        l = r = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, r - l + 1)


        
        return maxLength