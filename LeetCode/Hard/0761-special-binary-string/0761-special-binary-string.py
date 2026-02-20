class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        i = 0
        count = 0
        special_substrings = []
        
        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                inner = self.makeLargestSpecial(s[i+1:j])
                special_substrings.append('1' + inner + '0')
                i = j + 1
        
        special_substrings.sort(reverse=True)
        return ''.join(special_substrings)