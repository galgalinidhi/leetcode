class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        replace = -1
        for i in range(len(arr)-1,-1,-1):
            rightmax= max(arr[i], replace)
            arr[i]= replace
            replace = rightmax
        return arr    