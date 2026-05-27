class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        hashmap = {}

        for i in range(len(word)):
            s = word[i]

            if s.lower() == s or s not in hashmap:
                hashmap[s] = i

        for i in hashmap:
            s = i.lower()

            if i != s and s in hashmap and hashmap[s] < hashmap[i]:
                ans += 1

        return ans