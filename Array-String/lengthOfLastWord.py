class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arrayString = s.split()
        return len(arrayString[-1])
