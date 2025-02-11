class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        for c in ransomNote: 
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1
        
        return True

# use counter to keep track hashmap. first establishes hashmap counter, loop thru magazine, check if char is in the hashmap, if yes, then increase frequency, if not, set frequency to 1

# loop thru ransomNote and check if character in ransomNote existed in hashmap counter. If not, return False, if frequency is only 1 left, delete that character and if frequency more than 1, decrease frequency by 1
