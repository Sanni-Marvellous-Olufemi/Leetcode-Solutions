from heapq import heappush

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i] += 1

        arr = sorted(hashmap.keys())
        n = len(target)
        
        # 1. Match as many identical characters with target as possible
        matched_len = 0
        while matched_len < n and hashmap[target[matched_len]] > 0:
            hashmap[target[matched_len]] -= 1
            matched_len += 1
            
        # 2. Backtrack from matched_len down to 0
        for i in range(matched_len, -1, -1):
            if i < n:
                # Find smallest available character strictly greater than target[i]
                for j in arr:
                    if j > target[i] and hashmap[j] > 0:
                        ans = target[:i] + j
                        hashmap[j] -= 1
                        
                        # Append the rest of the available characters in sorted order
                        for k in arr:
                            while hashmap[k] > 0:
                                ans += k
                                hashmap[k] -= 1
                        return ans
            
            # Reclaim the character used at target[i - 1] for earlier backtracking
            if i > 0:
                hashmap[target[i - 1]] += 1
                
        return ""


class Solution1:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        hashmap = defaultdict(int)

        for i in s:
            hashmap[i] += 1

        arr = sorted(hashmap.keys())
        
        ans = ""
        for i in target:
            y = False

            for j in arr:
                if j >= i and hashmap[j] > 0:
                    y = True if j > i else False
                    ans += j
                    hashmap[j] -= 1
                    break
            else:
                return ""

            if y:
                break
        else:
            hashmap = defaultdict(int)
            heap = []
            y = False

            for i in range(len(ans)-1, -1, -1):
                if ans[i] not in hashmap:
                    heappush(heap, ans[i])
                hashmap[ans[i]] += 1

                for j in heap:
                    if j > target[i]:
                        ans = ans[:i]
                        hashmap[j] -= 1
                        ans += j
                        y = True
                        break

                if y:
                    break
            else:
                return ""
            
        for i in arr:
            while hashmap[i] > 0:
                ans += i
                hashmap[i] -= 1

        return ans
