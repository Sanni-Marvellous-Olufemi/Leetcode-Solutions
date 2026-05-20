class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        li = []
        hashmap = defaultdict(int)
        count = 0

        for i in range(len(A)):
            count += 1 if A[i] in hashmap else 0
            hashmap[A[i]] += 1
            
            count += 1 if B[i] in hashmap else 0
            hashmap[B[i]] += 1
            
            li.append(count)

        return li