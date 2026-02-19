class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # min for sub
        hashmap = defaultdict(int)

        start = ans = 0

        for i in range(len(s)):
            hashmap[s[i]] += 1

            if (hashmap["0"] and hashmap["1"]) and (i == len(s)-1 or s[i+1] != s[i]):
                ans += min(hashmap["0"], hashmap["1"])

                while s[start] != s[i]:
                    hashmap[s[start]] -= 1
                    start += 1

        return ans