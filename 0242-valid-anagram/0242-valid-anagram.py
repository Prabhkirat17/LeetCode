class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        count = collections.Counter(s)
        count.subtract(collections.Counter(t))
        for freq in count.values():
            if freq != 0:
                return False
        return True 