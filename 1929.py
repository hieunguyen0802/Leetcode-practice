
def getConcatenation(self, nums: List[int]) -> List[int]:
    # solution 1
    #return nums*2
    
    # solution 2 to works with third arg like concatenate x times 
    ans = []
    for i in range (2):
        for n in nums:
            ans.append(n)
    return ans        
    
    