class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in range(len(arr)):
            if arr.count(arr[i])==1:
                d[len(d)+1]=arr[i]
            else:
                continue
        if k in d:
            return d[k]
        return ""
