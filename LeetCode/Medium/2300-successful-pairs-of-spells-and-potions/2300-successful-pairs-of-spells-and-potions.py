class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []

        for i in spells:
            start, end, y = 0, len(potions)-1, False

            while start <= end:
                mid = (start + end) // 2

                if potions[mid] * i >= success and (mid == 0 or potions[mid-1] * i < success):
                    y = True
                    break

                if potions[mid] * i < success:
                    start = mid + 1
                else:
                    end = mid - 1

            ans.append(len(potions) - mid) if y else ans.append(0)

        return ans
                

 