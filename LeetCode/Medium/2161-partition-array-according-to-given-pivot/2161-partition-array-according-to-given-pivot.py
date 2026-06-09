class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, great, ans, count = [], [], [], 0

        for i in nums:
            if i < pivot:
                less.append(i)

            if i > pivot:
                great.append(i)

            count += 1 if i == pivot else 0

        for i in less:
            ans.append(i)

        for _ in range(count):
            ans.append(pivot)

        for i in great:
            ans.append(i)

        return ans
