class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        hashmap = defaultdict(list)
        ans = [-1 for i in queries]
        
        for i, num in enumerate(nums):
            hashmap[num].append(i)

        for idx, i in enumerate(queries):
            num = nums[i]
            arr = hashmap[num]

            if len(arr) <= 1:
                continue

            left, right = 0, len(arr)-1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == i:
                    prev, nexts = (mid-1) % len(arr), (mid+1) % len(arr)
                    
                    if nexts < mid:
                        ans[idx] = min(abs(arr[mid] - arr[prev]), abs(len(nums) - arr[mid] + arr[nexts]))

                    elif prev > mid:
                        ans[idx] = min(abs(arr[mid] + len(nums) - arr[prev]), abs(arr[mid] - arr[nexts]))
                    
                    else:
                        ans[idx] = min(abs(arr[mid] - arr[prev]), abs(arr[mid] - arr[nexts]))
                        
                    break

                if arr[mid] < i:
                    left = mid + 1

                if arr[mid] > i:
                    right = mid - 1

        return ans