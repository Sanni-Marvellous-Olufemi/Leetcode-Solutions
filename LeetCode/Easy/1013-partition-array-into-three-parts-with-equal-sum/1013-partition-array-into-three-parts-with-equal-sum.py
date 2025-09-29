class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False

        sums, count, tar = 0, 0, sum(arr)//3

        for i in range(len(arr)):
            if sums + arr[i] == tar:
                sums = 0
                count += 1
            else:
                sums += arr[i]
            if count == 2 and i < len(arr)-1:
                return True 

        return True if count == 3 else False