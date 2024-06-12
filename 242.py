#solution 1: count each element in s / t, store in hashset [value, appearance of value]. Then compare. -> time: o(n) space: o(n)

#solution 2: sort s and t then compare. -> time: o(n log n) space: o(1) 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1 
        # if (len(s) != len(t)): return False

        # countS, countT = {}, {}
        
        # for i in range (len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)  
        
        # for c in countS:
        #     if countS[c] != countT.get(c,0):
        #         return False
        # return True

        # solution 1*
        # return Counter(s) == Counter(t)

        # solution 2:
        return sorted(s) == sorted(t)
