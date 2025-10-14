class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        hashmap = {
            1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 
            9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 
            15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 
            20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 
            80:"Eighty", 90:"Ninety", 100:"Hundred", 1000:"Thousand", 1000000:"Million",    
            1000000000:"Billion"
            }
        arr = [
            1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20, 19, 18, 17, 16, 15, 
            14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        ]

        def walk(num, i):
            if num == 0:
                return ""

            if num <= 10:
                return hashmap[num]

            
            while i < len(arr) and num < arr[i]:
                i += 1

            log = num - arr[i] * (num//arr[i])
            part2 = walk(log, i)
            num = num - log
    
            
            if num in hashmap:
                part1 = hashmap[num] if num != 10 ** int(math.log10(num)) else "One" + " " + hashmap[num]
                
            else:
                if num//arr[i] in hashmap:
                    part1 = hashmap[num//arr[i]] + " " + hashmap[arr[i]]   
                else:
                    part1 = walk(num//arr[i], i) + " " + hashmap[arr[i]] 
                    

            return part1 + " " + part2 if part2 else part1 + part2

        return walk(num, 0)
