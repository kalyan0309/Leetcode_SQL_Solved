class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = Counter((s1.split())+(s2.split()))
        return [i for i,j in s.items() if j==1 ]
