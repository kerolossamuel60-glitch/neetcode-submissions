class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result=sorted(s)
        is_same=sorted(t)
        return result==is_same