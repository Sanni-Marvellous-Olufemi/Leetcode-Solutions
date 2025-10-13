class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans, sets = [], set()
        def ord_set(word):
            arr = [0] * 26
            
            for i in word:
                arr[ord(i) - ord("a")] += 1

            return arr

        for word in words:
            chars = ord_set(word)
            if tuple(chars) in sets:
                continue
            sets.add(tuple(chars))
            ans.append(word)

        return ans
        