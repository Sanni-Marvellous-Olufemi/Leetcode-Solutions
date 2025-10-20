class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


                    

"""
 1 -> 3 -> 2 -> 4 -> 2
                ^    |
                | <- v


3 -> 4 -> 2 -> 3 -> 
                   |
     ^             v
     |      <-


[1,3,4,2,2]

[3,1,3,4,2]
 0 1 2 3 4
s = 3, f = 3
s = 4, f = 2
s = 2, f = 4
s = 3, f = 3
"""