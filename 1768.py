# solution: loop thru the smaller list and append both char in both lists. Then findout which list still has remains, then append to the answer.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenToGo = min(len(word1), len(word2))
        ans = ''
        for i in range(lenToGo):
            ans = ans + word1[i] + word2[i]

        if len(word1) == lenToGo:
            ans = ans + word2[lenToGo:]
        if len(word2) == lenToGo:
            ans = ans + word1[lenToGo:]
  
        return ans
        

