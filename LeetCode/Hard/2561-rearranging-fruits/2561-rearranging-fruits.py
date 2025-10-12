from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)
        heap = []
        mean1, mean2 = min(basket1), min(basket2)
        mean = min(mean1, mean2)

        for i in range(len(basket1)):
            hashmap1[basket1[i]] += 1
            hashmap2[basket2[i]] += 1

        for i in hashmap1:
            if i in hashmap2 and (hashmap1[i] + hashmap2[i]) % 2 != 0:
                return -1
            if i not in hashmap2 and hashmap1[i] % 2 != 0:
                return -1

            if hashmap1[i] != hashmap2[i]:
                count = abs(hashmap1[i] - hashmap2[i]) // 2
                for j in range(count):
                    heap.append(i)
            elif i not in hashmap2:
                count = hashmap1[i] // 2
                for j in range(count):
                    heap.append(i)

        for i in hashmap2:
            if i not in hashmap1 and hashmap2[i] % 2 != 0:
                return -1
            
            if i not in hashmap1:
                count = hashmap2[i] // 2
                for j in range(count):
                    heap.append(i)

        count = 0
        heap.sort()
        for i in range(len(heap)//2):
            if heap[i] == mean:
                count += mean
                continue

            count += min(heap[i], mean * 2)
            


        return count

"""
[4,4,4,4,1,1]. 4-2 = 2/2 = 1
[1,1,1,1,4,4]. 4-2 = 2/2 = 1
[4,1]
[4,4,5,6]
[10,10,20,30]
"""

        