class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        hashmap = defaultdict(int)
        left, y = 0, False

        for right in range(len(s)):
            sets = set(s[left:right+1])

            if right - left + 1 == minSize:
                if len(sets) <= maxLetters:
                    hashmap[s[left:right+1]] += 1
                    
                left += 1

        
        return max(hashmap.values()) if hashmap else 0


