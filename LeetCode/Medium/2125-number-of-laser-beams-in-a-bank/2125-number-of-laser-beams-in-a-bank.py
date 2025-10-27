class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr = []

        for i in range(len(bank)):
            count = 0
            for j in bank[i]:
                if j == "1":
                    count += 1
            if count:
                arr.append(count)

        ans = 0
        for i in range(len(arr) - 1):
            ans += arr[i] * arr[i+1]

        return ans

                
        