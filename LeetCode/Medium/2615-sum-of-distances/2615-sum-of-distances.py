class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0 for i in nums]
        hashmap = defaultdict(list)

        for i in range(len(nums)):
            hashmap[nums[i]].append(i)

        for key in hashmap:
            curr = hashmap[key]
            pref = [curr[0]]
            n = len(curr)

            for i in range(1, n):
                pref.append(curr[i] + pref[i-1])
            
            for i in range(n):
                idx = curr[i]

                right = (pref[-1] - pref[i]) - (idx * (n - i - 1)) if i < n-1 else 0
                left = (idx * i) - pref[i-1] if i > 0 else 0

                ans[curr[i]] = right + left

        return ans