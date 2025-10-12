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
            if i not in memo:
                walk(i)

        return ans


        

"""
-Use a hashmap to store the frequency of each damage
-Remove all duplicates in power (Create a new power without duplicates)
-Sort the new power in decreasing order
-Recursively go down starting from index 0 (highest damage in power) to valid damages that can be added (all damages less than power[j] - 2)
-In the recursive function, the base case is if index is invalid (return 0) or index is the last thing in the list (return power[i] * freq in hashmap) or index is in memo (already been traversed, return memo[i]).
-For the recusuve case, 
-Find the next valid danger (While power[i+1] == power[i] -2 or -1, skip. runs in O(1) due to no duplicate). 
-When you finally get to a valid danger, if the next 2 elements after that danger are in the range (danger -1, -2) recursively call walk on each of the indices(use 0-1 knapsack to get the maximum).
-We check the next 2 elements because picking the first valid danger automatically skips the next 2 if they are in the range (danger -1, -2), so you want to check each of the outcomes to see the best, not just greedily picking the highest and skipping the rest
-After recursively calling walk on the 3 indices (if they're valid else assign them to 0) pick the one with the max total damage and add the value + the current i * freq to memo (memo[i] = max(opt1, opt2, opt3) + (power[i] * hashmap[power[i]])) and return it
-Now in the main function, call walk on all indices that have not been walked on
-Return the max total damage in memo after all operations
"""