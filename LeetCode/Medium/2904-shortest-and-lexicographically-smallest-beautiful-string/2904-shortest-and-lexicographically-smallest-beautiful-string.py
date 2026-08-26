class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = "1" * (len(s) + 1)
        pref = [0] * (len(s) + 1)
        count = 0

        for i in range(1, len(pref)):
            count += int(s[i-1])
            pref[i] += count

        left = 0

        for right in range(len(pref)):
            while pref[right] - pref[left] == k:
                if len(ans) > right-left:
                    ans = s[left:right] 
                elif len(ans) == (right-left):
                    ans = min(ans, s[left:right])

                left += 1

        return ans if len(ans) <= len(s) else ""