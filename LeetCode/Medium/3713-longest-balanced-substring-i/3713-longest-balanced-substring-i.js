class Solution1:
    def longestBalanced(self, s: str) -> int:
        pref = [] 
        a, b, c, n = 0, 0, 0, len(s)
        ans = 0

        for i in range(n):
            a += 1 if s[i] == "a" else 0
            b += 1 if s[i] == "b" else 0
            c += 1 if s[i] == "c" else 0

            pref.append([a,b,c])

        for i in range(n-1, -1, -1):
            a, b, c = pref[i]
            curr = i - (min(a,b,c) * 3) + 1
            print(curr, i)
            e, f, g = pref[curr]

            if (a-e) == (b-f) == (c-g):
                ans = max(ans, (a-e) + (b-f) + (c-g))

        return ans

