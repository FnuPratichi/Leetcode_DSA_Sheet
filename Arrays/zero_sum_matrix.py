# m*n matrix
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],
#          [0,4,5,0],
#          [0,3,1,0]]

if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    m = len(matrix)    #row
    n = len(matrix[0]) #col
    print(m,n)

col_mark = ['zero']* n
row_mark = ['zero']* m

def setZeroes(matrix):
    for row in range(0,m):
        for col in range(0,n):
            if matrix[row][col]==0:
                row_mark[row]="marked"
                col_mark[col]="marked"
    
    for row in range(0,m):
        for col in range(0,n):
            if row_mark[row] == "marked" or col_mark[col]== "marked":
                matrix[row][col] = 0
    print(matrix)
setZeroes(matrix)
