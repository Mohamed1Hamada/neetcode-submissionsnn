class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if len(s) != len(t):
            return False

        box = {}

        for a, b in zip(s, t):
            box[a] = box.get(a, 0) + 1    
            box[b] = box.get(b, 0) - 1    

        
        return all(v == 0 for v in box.values())
