class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        
        def ord_set(word):
            arr = [0] * 26
            
            for i in word:
                arr[ord(i) - ord("a")] += 1

            return arr

        for i in range(1, len(words)):
            if ord_set(words[i]) == ord_set(words[i-1]):
                continue
            ans.append(words[i])

        return ans
        