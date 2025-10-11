class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        ans = 0
        hashmap = Counter(power)
        power = []
        memo = {}

        for i in hashmap:
            power.append(i)

        power.sort(reverse = True)

        def walk(i):
            nonlocal ans

            if i >= len(power):
                return 0

            if i == len(power)-1:
                ans = max(ans, power[i] * hashmap[power[i]])
                return power[i] * hashmap[power[i]]

            if i in memo:
                return memo[i]

            j = i + 1
            while j < len(power):
                if power[i] - 2 > power[j]:
                    break
                j += 1
            
            if (j < len(power)-2) and (power[j+1] >= power[j] - 2) and (power[j+2] >= power[j] - 2):
                opt1 = walk(j)
                opt2 = walk(j+1)
                opt3 = walk(j+2)
            elif j < len(power)-1 and (power[j+1] >= power[j] - 2):
                opt1 = walk(j)
                opt2 = walk(j+1)
                opt3 = 0
            else:
                opt1 = walk(j)
                opt2 = 0
                opt3 = 0

            
            memo[i] = max(opt1, opt2, opt3) + (power[i] * hashmap[power[i]])
            ans = max(ans, memo[i])
            return memo[i]

        for i in range(len(power)):
            if power[i] not in memo:
                walk(i)

        return ans


        

"""
-Recursively go down, use a while loop. While power i+1 == curr +2 or +1, skip. when you finally get to something less than curr - 2, if the next of that is in the range (+1, +2) use 0-1 knapsack to get the maximum
-Store max of each in a memo and return it
"""