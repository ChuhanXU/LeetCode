
def matrixSearch(matrix,target):
    if matrix:
        row = len(matrix)-1
        col=0
        width = len(matrix[0])
        while row>=0 and col<width:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                row-=1
            else:
                col+=1
    return False

matrix=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 17
print(matrixSearch(matrix,target))