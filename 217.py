# blind 75 problems
# solution 1: brute force
# loop twice and check duplicate. Time: O(n2) Space: O(1)

# solution 2: sort then remove duplicate (adjacent). Time: O(nLogn) Space: O(1)

# solution 3: using hashset. Time: O(n) Space: O(n)

def solution(self, nums: List[int]) -> bool:
    hashset = set()
    
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
        
    return False