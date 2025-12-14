class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, dummy, sets = [], [], set()
        nums.sort()

        def walk(i):
            if tuple(dummy) in sets:
                return 
            else:
                sets.add(tuple(dummy))

            ans.append(dummy[:])

            for j in range(i, len(nums)):
                dummy.append(nums[j])
                walk(j+1)
                dummy.pop()

        walk(0)
        return ans


# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         ans, dummy = [[]], []
#         nums.sort()

#         def walk(i):
#             for j in range(i+1, len(nums)):
#                 dummy.append(nums[j])
#                 ans.append(dummy[:])
#                 walk(j)
#                 dummy.pop()

        
#         for i in range(len(nums)):
#             if (i > 0) and (nums[i] == nums[i-1]):
#                 continue

#             dummy.append(nums[i])
#             ans.append(dummy[:])
#             walk(i)
#             dummy.pop()
            
#         return ans