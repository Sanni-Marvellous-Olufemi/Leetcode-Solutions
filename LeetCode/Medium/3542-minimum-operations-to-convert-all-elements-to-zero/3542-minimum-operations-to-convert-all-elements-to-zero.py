class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count, stack = 0, []

        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                continue

            if stack and i != len(nums)-1:
                while stack and nums[i] < stack[-1]:
                    stack.pop()
                    count += 1
                stack.append(nums[i])
            else:
                stack.append(nums[i])

        stack = set(stack)
        return count + len(stack) if 0 not in stack else count + len(stack) - 1
