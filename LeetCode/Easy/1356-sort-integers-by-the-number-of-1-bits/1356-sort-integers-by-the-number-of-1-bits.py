class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            arr[i] = (bin(arr[i]).count("1"), arr[i])

        arr.sort()
        arr = [j for i,j in arr]
        return arr