class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        '''
        T: O(n) and S: O(1)
        '''
        if not A: return []
        
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i, j = i + 1, j - 1
            else:
                if A[i] % 2 == 0:
                    i += 1
                if A[j] % 2 == 1:
                    j -= 1
        return A
