class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix[0])*len(matrix)-1

        while l<=r:

            m=(l+r)//2

            i=m//(len(matrix[0]))
            j=m%(len(matrix[0]))
            

            m_num=matrix[i][j]

            if target==m_num:
                return True

            elif target<m_num:
                r=m-1
            
            else:
                l=m+1
        return False



        