"""
def binary_search(x, left, right):
    start = left + 1
    end = right - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == (0 - x):
            return [nums[left], nums[mid], nums[right]]
        elif nums[mid] < (0 - x):
            start = mid + 1
        elif nums[mid] > (0 - x):
            end = mid - 1
    return None


def threesum(x, left, right):

    while abs(x) <= nums[right]:
        var = binary_search(x, left, right):
        if var:
            ans.append(var)
        
        right -= 1
        x = nums[right] + nums[left]
""" 
from collections import defaultdict       

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left, right = 0, (len(nums) - 1)
        ans, hashmap = [], defaultdict(int)
        sets = set()


        if nums[0] == 0 and nums[2] == 0:
            return [[0,0,0]]

        for i in nums:
            hashmap[i] += 1


        def threesum(x, left, right):

            while abs(x) <= nums[right] and right > left + 1:
                hashmap2[nums[right]] -= 1

                if -x in hashmap2 and hashmap2[-x] > 0:
                    if tuple([nums[left], -x, nums[right]]) not in sets:
                        ans.append([nums[left], -x, nums[right]])
                        sets.add(tuple([nums[left], -x, nums[right]]))
                    
                right -= 1
                x = nums[right] + nums[left]
                



        for left in range(len(nums)):
            x = nums[right] + nums[left]
            if abs(x) > nums[right] or (nums[left] == nums[left-1] and left != 0):
                hashmap[nums[left]] -= 1
                continue 
            

            hashmap[nums[left]] -= 1
            hashmap2 = hashmap
            threesum(x, left, right)

            while nums[right] == nums[right-1] and right > 0:
                right -= 1
                hashmap[nums[right]] -= 1

        return ans

"""
[-4, -1, -1, 0, 1, 2] if abs(left + right > right or < left)

[-1, 0, 1, 2, 3, 5]
[-5, -4, -1, -1, 0, 1, 2, 3, 4, 5]


"""
        
        