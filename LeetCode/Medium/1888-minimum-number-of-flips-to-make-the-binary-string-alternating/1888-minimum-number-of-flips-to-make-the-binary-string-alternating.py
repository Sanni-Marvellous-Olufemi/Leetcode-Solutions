class Solution:
    def minFlips(self, s: str) -> int:
        one = zero = 0
        hashmap = defaultdict(int)

        for i in range(len(s)):
           one += 1 if (i % 2 == 0 and s[i] == "1") else 0
           zero += 1 if (i % 2 == 1 and s[i] == "0") else 0 
           hashmap[s[i]] += 1

        ans = min(one+zero, len(s)-(one+zero))
        if len(s) % 2 == 0:
            return ans

        for i in range(len(s)):
            if s[i] == "0":
                one = hashmap["1"] - one
                zero = hashmap["0"] - zero - 1
            else:
                zero = hashmap["0"] - zero
                one = hashmap["1"] - one + 1

            ans = min(ans, min(one+zero, len(s)-(one+zero)))

        return ans

        