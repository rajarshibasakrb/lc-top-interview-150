  class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)  
        if n != 0:
            h = 0
            citations.sort(reverse=True)
            while (h < n and citations[h] - 1 >= h):
                h += 1
            return h
        else:
            return 0
