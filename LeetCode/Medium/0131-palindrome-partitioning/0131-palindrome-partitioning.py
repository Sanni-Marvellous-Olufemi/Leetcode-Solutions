class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        sets = set()

        def isPalindrome(word):
            left, right = 0, len(word)-1

            while left <= right:
                if word[left] != word[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True if word else False

        def walk(i, path, curr):
            if i >= len(s):
                if isPalindrome(curr):
                    if tuple(path + [curr]) not in sets:
                        ans.append(path + [curr])
                        sets.add(tuple(path + [curr]))
                if not curr and tuple(path) not in sets:
                    ans.append(path)
                    sets.add(tuple(path))
                return

            curr += s[i]

            if isPalindrome(curr):
                walk(i+1, path+[curr], "")

            walk(i+1, path, curr)

        walk(0, [], "")
        return ans