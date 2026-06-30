class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashmap = defaultdict(deque)
        ans = 0

        for i in range(len(s)):
            hashmap[s[i]].append(i)

        for i in range(len(s)):
            if not hashmap["a"] or not hashmap["b"] or not hashmap["c"]:
                break

            num = max(hashmap["a"][0], hashmap["b"][0], hashmap["c"][0])
            ans += len(s) - num
            hashmap[s[i]].popleft()

        return ans
            
