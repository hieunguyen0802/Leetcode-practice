# solution: define S, T as len(s,t). 2 base cases. Have two pointer, i for t and j for s. if s[j] == t[i], move to next char, otherwise keep moving i in T. If j reach the end, return True


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        
        if s == '': return True
        if S > T : return False
        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S - 1:
                    return True
                j+=1
        return False 
